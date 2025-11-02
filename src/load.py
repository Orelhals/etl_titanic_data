import pandas as pd

def load_to_csv(df, path="data/clean_titanic.csv"):
    df.to_csv(path, index=False)
    print(f"✅ Dados salvos em {path}")


