import os
from scipy.spatial.distance import cdist


def compute_distance(embeddings1, embeddings2, audio_folder, image_folder):
    audio_files = os.listdir(audio_folder) if os.path.isdir(audio_folder) else []
    image_files = os.listdir(image_folder) if os.path.isdir(image_folder) else []

    distance_dict = {}

    for i in range(len(embeddings2)):
        audio_file = os.path.basename(audio_files[i]) if i < len(audio_files) else None
        image_file = os.path.basename(image_files[i]) if i < len(image_files) else None
        distance = cdist([embeddings1], [embeddings2[i]], metric='euclidean')[0][0]
        distance_dict[audio_file] = {
            'image_file': image_file,
            'distance': distance
        }

    return distance_dict







