import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='specify data amount')
args = parser.parse_args()
if args.data:
    n = int(args.data)
else:
    n = 1000

X = np.random.randn(n,4)
noise = np.random.randn(n)/20
y = np.sum(X * [1,2,3,4], axis=1) + noise
df = pd.DataFrame(X, columns=['x1', 'x2', 'x3', 'x4'])
df['target'] = y
for col in df.columns:
    df[col] = "'"+df[col].astype(str)+"'"

df.to_csv('data.csv')
