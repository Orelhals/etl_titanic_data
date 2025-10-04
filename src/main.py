from extract import extract_data
# from transform import clean_data
# from load import load_data
from extract import extract_data

def main():
    raw = extract_data()
    print("First 5 records:\n", raw.head())
    
    # clean = clean_data(raw)
    # load_data(clean)

if __name__ == "__main__":
    main()

