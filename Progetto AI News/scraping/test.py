import pandas as pd

df = pd.read_csv("database.csv", sep="\t")
dati = df.values.tolist()

print(len(dati))
