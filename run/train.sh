#!/usr/bin/env bash

dvc run -d cleaned_data.csv \
        -d train.py \
        -o linear_regressor.joblib \
        -f run/train.dvc \
	-M mse.json \
	-M coefs.json \
	-M n_data.json \
        python train.py 
