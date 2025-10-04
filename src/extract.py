import pandas as pd 
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Nome do arquivo dentro do dataset (confira no Kaggle!)
file_path = "tested.csv"

def extract_data() :
    # Carregar dataset
    df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "brendan45774/test-file",
    file_path,
    )
    return df

