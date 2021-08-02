#!/bin/bash

cd train_run1 
sbatch submit.sb 

cd ../train_run2 
sbatch submit.sb 

cd ../train_run3 
sbatch submit.sb 

cd ../train_run4 
sbatch submit.sb 

cd ../train_run5 
sbatch submit.sb


