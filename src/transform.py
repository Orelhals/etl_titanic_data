import pandas as pd
from extract import extract_data
#Processo ETL:
def fill_missing_values(df):
    # Calculando a mediana que vai substituir os valores nulos da coluna age.
    #Preenchendo valores nulos
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    return df

def drop_irrelevant_columns(df):
    #! Método drop tira os tipos especificados
    #removendo colunas irrelevantes
    df = df.drop(columns=['PassengerId','Name','Ticket','Cabin'])
    return df

def encode_sex(df):
    #transforando masculino e feminino em binário pra ajudar numa possível análise:
    df['Sex'] = df['Sex'].map({'male' : 1, 'female' : 0})
    return df

def transform_data(df):

    #* EDA = Exploratory Data Analysis (Análise Exploratória de Dados).
    print("🔹 Informações iniciais:")
    print(df.info())
    print(df.describe())

    print("\n✅ Dados transformados:")
    df = fill_missing_values(df)
    df = drop_irrelevant_columns(df)
    df = encode_sex(df)
    
    #?Após conferirmos, vimos que os valores nulos nas idades foram substituidos pela mediana dos nao nulos
    print("Missing values: ", df.isnull().sum())
    print(df.head())
    return df

#Cria colunas para cada subconjuto de zona das embarque, one-hot enconding: true or false para as categorias se fizerem parte do portao de embarque correto.
def prepare_for_ml(df):
    df = pd.get_dummies(df , columns=['Embarked'], prefix='Embarked')
    return df

#Serve para apenas executar se eu rodar o arquivo.
if __name__ == "__main__":
    df = extract_data()
    df_final = transform_data(df)