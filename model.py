import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('cleaned_data.csv')
y = df['target']
X = df.drop('target')

reg = LinearRegression().fit(X,y)
score = reg.score(X,y)
