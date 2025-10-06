import pandas as pd 
from extract import extract_data

#value_count()

df = extract_data()
# sex_number = df["Sex"].value_counts()
# print(sex_number)

#fazer uma função que calcule o número de sobrevivente de cada sexo.

#* EDA = Exploratory Data Analysis (Análise Exploratória de Dados).
print(df.info())
print(df.describe())

print("Missing values: ", df.isnull().sum())
#?86 valores nulos age/ 327 nulos em cabin

#*Processo ETL:

#! Método drop tira os tipos especificados
df = df.drop(columns=['PassengerId','Name','Ticket','Cabin'])
print(df.head())
print(df.shape)