#!/bin/bash
# @job_name = distance_burger_2py
# @class = lowprio
# @initialdir = . 
# @output = file1.out
# @error = file1.err
# @total_tasks = 4
# @wall_clock_limit = 4-00:00:00

module load gcc/4.9.3
module load PYTHON/3.6.3

python3 irune.py ../../iruiz/Burger_Gorilla/READ/CHROMS/All_annotated_gorilla.vcf.gz own_scr.mat 

