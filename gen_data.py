import numpy as np
import pandas as pd

X = np.random.randn(1000,4)
noise = np.random.randn(1000)/20
y = np.sum(X, axis=1) + noise
df = pd.DataFrame(X, columns=['x1', 'x2', 'x3', 'x4'])
df['target'] = y
for col in df.columns:
    df[col] = "'"+df[col].astype(str)+"'"

df.to_csv('data.csv')
