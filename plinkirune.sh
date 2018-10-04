#!/bin/bash
# @job_name = plinkirune
# @initialdir = .
# @output = plink.out
# @error = plink.err
# @total_tasks = 4
# @wall_clock_limit = 22:00:00

module load intel/16.3.067
module load lapack/3.2.1
module load zlib/1.2.8
module load PLINK/1.90b

plink --vcf downsampling/All_annotated_gorilla.vcf.gz --double-id --keep sample_plink.list --distance ibs 1-ibs --out results_mydown/plink_matrix
