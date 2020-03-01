from joblib import load

reg = load('linear_regressor.joblib')
print(reg.coef_)
