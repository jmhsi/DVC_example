# %load model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump
import json

df = pd.read_csv('cleaned_data.csv', index_col=0)
train = df[:-2]
valid = df[-2:]
y_train = train['target']
X_train = train.drop('target', axis=1)
y_valid = valid['target']
X_valid = valid.drop('target', axis=1)

reg = LinearRegression().fit(X_train,y_train)
y_pred = reg.predict(X_valid)
mse = mean_squared_error(y_valid, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'Coefficients: {reg.coef_}')
      
# save model
dump(reg, 'linear_regressor.joblib')

# write metrics
with open('mse.json', 'w+') as f:
    json.dump({'mse':mse}, f)
