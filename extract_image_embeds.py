import pandas as pd
import data
import torch
from models import imagebind_model
from models.imagebind_model import ModalityType
import os
import numpy as np
from tqdm import tqdm


def get_image_embedding(image_folder):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Get list of strings from audio folder
    image_files = os.listdir(image_folder)
    image_paths = [os.path.join(image_folder, file) for file in image_files]

    # Instantiate model
    model = imagebind_model.imagebind_huge(pretrained=True)
    model.eval()
    model.to(device)

    # Initialize a list to store the embeddings
    embeddings_list = []
    #print(len(image_paths))
    # Process each audio file
    for image_path in tqdm(image_paths):
        inputs = {
            ModalityType.VISION: data.load_and_transform_vision_data([image_path], device)
        }

        with torch.no_grad():
            embeddings = model(inputs)
            image_embedding = embeddings[ModalityType.VISION].cpu().numpy()
            embeddings_list.append(image_embedding.flatten())  # Append the flattened embedding to the list

    # Convert the list of embeddings to a numpy array
    embeddings_array = np.stack(embeddings_list)

    return embeddings_array

