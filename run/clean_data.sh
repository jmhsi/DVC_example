#!/usr/bin/env bash

dvc run -d data.csv \
        -d clean_data.py \
        -o cleaned_data.csv \
        -f run/clean_data.dvc \
        python clean_data.py 
