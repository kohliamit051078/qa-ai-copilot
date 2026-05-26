import pandas as pd
df = pd.read_excel("Data/test.xlsx", engine="openpyxl")
print(df.head())

