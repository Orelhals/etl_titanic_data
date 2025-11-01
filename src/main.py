from extract import extract_data
from transform import transform_data, prepare_for_ml
# from transform import clean_data
# from load import load_data

def main():
    raw = extract_data()
    print("Dados extraídos:\n")
    print(raw.head())

    clean = transform_data(raw)
    print("Dados em tratamento:\n")
    print(clean.head())

    df_ml = prepare_for_ml(clean)
    print(df_ml.head())
    
    # clean = clean_data(raw)
    # load_data(clean)

if __name__ == "__main__":
    main()

