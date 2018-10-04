#!/bin/bash
# @job_name = distance_burger_py
# @initialdir = . 
# @output = file1.out
# @error = file1.err
# @total_tasks = 4
# @wall_clock_limit = 23:00:00

module load gcc/4.9.3

#Command usage
./bin/VCF2Dis-1.10/bin/VCF2Dis -InPut downsampling/All_annotated_gorilla.vcf.gz -OutPut results_mydown/subpop_p_dis_hum.mat -SubPop sample.list
