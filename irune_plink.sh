#!/bin/bash
# @job_name = distance_burger_plink
# @initialdir = .
# @output = dist_burger_plink.out
# @error = dist_burger_plink.err
# @total_tasks = 4
# @wall_clock_limit = 23:00:00

module load gcc/4.9.3
module load PLINK

./plink --vcf ../../iruiz/Burger_Gorilla/READ/CHROMS/All_annotated_gorilla.vcf.gz --double-id --distance ibs 1-ibs
