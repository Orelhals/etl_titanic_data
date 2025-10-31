import pandas as pd 
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Nome do arquivo dentro do dataset (confira no Kaggle!)
file_path = "tested.csv"

def extract_data(dataset="brendan45774/test-file", file_path="tested.csv"):
    """Extrai os dados brutos do Kaggle e retorna um DataFrame pandas."""
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        dataset,
        file_path,
    )
    return df

