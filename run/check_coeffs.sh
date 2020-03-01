#!/usr/bin/env bash

dvc run -d linear_regressor.joblib \
        -d check_coeffs.py \
        -f run/check_coeffs.dvc \
        python check_coeffs.py 
