import os
import re
import requests
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def download_fits_files(folder_url, save_directory):
    """
    Download FITS files from a given folder URL and save them to the specified directory.

    Args:
        folder_url (str): The URL of the folder containing FITS files.
        save_directory (str): The directory where the FITS files will be saved.
    """
    response = requests.get(folder_url)
    fits_links = re.findall(r'href=[\'"](.*?\.fits(?:\.gz)?)', response.text)

    os.makedirs(save_directory, exist_ok=True)

    for link in fits_links:
        file_url = folder_url + link
        file_name = os.path.basename(link)
        print("Downloading:", file_url)
        with open(os.path.join(save_directory, file_name), 'wb') as f:
            f.write(requests.get(file_url).content)
        print("Downloaded.")
        
# Función para plotear PCA
def plot_pca(X, n_components):
    pca = PCA(n_components=n_components)
    pca.fit(X)
    X_pca = pca.transform(X)
    print("Resultados de la transformada PCA:")
    print(X_pca)
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.title('PCA visualization')
    plt.show()
