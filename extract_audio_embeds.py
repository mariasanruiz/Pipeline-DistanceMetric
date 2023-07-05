import pandas as pd
import data
import torch
from models import imagebind_model
from models.imagebind_model import ModalityType
import os
import numpy as np
from tqdm import tqdm

def get_audio_embedding(audio_folder):

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Get list of strings from audio folder
    audio_files = os.listdir(audio_folder)
    audio_paths = [os.path.join(audio_folder, file) for file in audio_files]

    # Instantiate model
    model = imagebind_model.imagebind_huge(pretrained=True)
    model.eval()
    model.to(device)

    # Initialize a list to store the embeddings
    embeddings_list = []

    # Process each audio file
    for audio_path in tqdm(audio_paths):
        inputs = {
            ModalityType.AUDIO: data.load_and_transform_audio_data([audio_path], device)
        }

        with torch.no_grad():
            embeddings = model(inputs)
            audio_embedding = embeddings[ModalityType.AUDIO].cpu().numpy()
            embeddings_list.append(audio_embedding.flatten())  # Append the flattened embedding to the list

    # Convert the list of embeddings to a numpy array
    embeddings_array = np.stack(embeddings_list)
    return embeddings_array
