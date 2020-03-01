#!/usr/bin/env bash

dvc run -d cleaned_data.csv \
        -d train.py \
        -o linear_regressor.joblib \
        -f run/train.dvc \
	-M mse.json \
        python train.py 
