# %load clean_data.py
import pandas as pd

df = pd.read_csv('data.csv', index_col=0)
print('Original Data format (note data is strings):')
print(df)
print('Turn strings into ints and write out cleaned_data.csv')
for col in df.columns:
    df[col] = df[col].str.replace("'", "").astype(float)
print(df)
df.to_csv('cleaned_data.csv')
