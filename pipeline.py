import numpy as np
from extract_image_embeds import get_image_embedding
from extract_audio_embeds import get_audio_embedding
from slerp import slerp
from distances import compute_distance
import os
import argparse

# Execute the following command:
# python pipeline.py --ref_image /home/byo/ImageBind/pycharm_project_242/ref_000750 --ref_audio /tmp/pycharm_project_43/ImageBind-main/gener_files/Playing_With_Embeds/high-quality/ref_audios/fragmentos/ --ob_image /tmp/pycharm_project_43/ImageBind-main/gener_files/Playing_With_Embeds/high-quality/SUPER-ELDER-SKYRIM-FRAMES/ref_000750/ --gen_audio /home/byo/Amazon/maria/ImageBindProject/ImageBind-main/skyrim_audios_prueba

parser = argparse.ArgumentParser(description='Audio-Generation Evaluation Metric Pipeline')
parser.add_argument('--ref_image', type=str, help='Path to the reference image')
parser.add_argument('--ref_audio', type=str, help='Path to the reference audio')
parser.add_argument('--ob_image', type=str, help='Path to objective image folder')
parser.add_argument('--gen_audio', type=str, help='Path to generated audio folder')

args = parser.parse_args()

# Only one reference image
ref_image_folder = args.ref_image
if not os.path.exists(ref_image_folder):
    print("Reference image file path does not exist. Please try again.")
    exit(1)
# Only one reference audio
ref_audio_folder = args.ref_audio
if not os.path.exists(ref_audio_folder):
    print("Reference audio file path does not exist. Please try again.")
    exit(1)
# N objective images (same number of objective images as target audios)
obj_image_folder = args.ob_image
if not os.path.exists(obj_image_folder):
    print("Objective image folder path does not exist. Please try again.")
    exit(1)
# N target audios (same number of target audios as objective images)
target_audio_folder = args.gen_audio
if not os.path.exists(target_audio_folder):
    print("Generated audio folder path does not exist. Please try again.")
    exit(1)


# Extract ref image embedding
ref_image_embedding = get_image_embedding(ref_image_folder)

# Extract ref audio embedding
ref_audio_embedding = get_audio_embedding(ref_audio_folder)

# z1frames (imágenes objetivo - N)
obj_image_embedding = get_image_embedding(obj_image_folder)

# z1audio (audios we want to compare - audios Laura takes from each translator - N)
target_audio_embedding = get_audio_embedding(target_audio_folder)

# slerp (change t=0.5 for a value between 0 and 1 if required)
interpolated_img_embedding = slerp(ref_image_embedding[0], obj_image_embedding, 0.5)

# z*1audio (the 'perfect' audio - N)
for interpolated_embedding in interpolated_img_embedding:
    obj_audio_embedding = np.add(ref_audio_embedding[0], interpolated_embedding)


# métrica de distancia (returns the index of the closest) ??? queremos esto o queremos que devuelva la distancia en forma de embed ??????
distance_dict = compute_distance(obj_audio_embedding, target_audio_embedding, target_audio_folder, obj_image_folder)

# Accessing the computed distances
for audio_file, data in distance_dict.items():
    image_file = data['image_file']
    distance = data['distance']
    print(f"Audio file: {audio_file}, Image file: {image_file}, Distance: {distance}")