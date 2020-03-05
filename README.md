# DVC_example
DVC example for Data Science in Context DATA 607

# Make some data
`python gen_data -d <n_datapoints> -c <c1,c2,c3,c4>` (c1-c4 are coefficients that the linear regressor should find)

# Example use cases
`git checkout <branch>` data.csv.dvc (checkout the dvc pointer from a specific branch/point in time)\
`dvc checkout` (dvc sees the pointer has changed, pulls in the right version of data.csv from the dvc cache)\
`dvc repro run/check_coeffs.dvc` (dvc reproduces the pipeline up to the stage specified.)

# If you need to alter stages of the pipeline
# Here you define the stages, their dependencies, and their outputs
# See dvc documentation for more info
make changes to `run/<stage-definition-file>.sh` files\
`bash run/<stage-definition-file>.sh`
