# scripts/data_collection.py

import pandas as pd
import os

def download_and_save_data():
    """
    Load Kaggle YouTube trending dataset and save it as raw_data.csv
    """
    # Make sure the data directory exists
    #os.makedirs("../data", exist_ok=True)

    # Assuming you manually download the file from Kaggle
    # For example, 'USvideos.csv' from 'Trending YouTube Video Statistics' dataset
    dataset_path = "../data/USvideos/USvideos.csv"  # Update this if needed

    try:
        df = pd.read_csv(dataset_path, encoding='utf-8')
        df.to_csv("../data/raw_data.csv", index=False)
        print("Raw data saved to ../data/raw_data.csv")
    except Exception as e:
        print(f"Error loading dataset: {e}")

if __name__ == "__main__":
    download_and_save_data()


