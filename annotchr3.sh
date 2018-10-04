#!/bin/bash
# @job_name = downsampling
# @initialdir = .
# @output = down.out
# @error = down.err
# @total_tasks = 4
# @wall_clock_limit = 23:00:00

module load oscar-modules/1.0.3 
module load gcc/4.9.3-gold
module load zlib/1.2.8  
module load HTSLIB/latest
module load VCFTOOLS/0.1.12

tabix -h /scratch/devel/iruiz/Burger_Gorilla/READ/ASCERTAIN/All.gor.vcf.gz chr3 | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L894_burger_annotations.bed.gz -d key=INFO,ID=L894_burger,Number=1,Type=String,Description='L894_burger allele' -c CHROM,FROM,TO,INFO/L894_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L897_burger_annotations.bed.gz -d key=INFO,ID=L897_burger,Number=1,Type=String,Description='L897_burger allele' -c CHROM,FROM,TO,INFO/L897_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L898_burger_annotations.bed.gz -d key=INFO,ID=L898_burger,Number=1,Type=String,Description='L898_burger allele' -c CHROM,FROM,TO,INFO/L898_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L904_burger_annotations.bed.gz -d key=INFO,ID=L904_burger,Number=1,Type=String,Description='L904_burger allele' -c CHROM,FROM,TO,INFO/L904_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L896_burger_annotations.bed.gz -d key=INFO,ID=L896_burger,Number=1,Type=String,Description='L896_burger allele' -c CHROM,FROM,TO,INFO/L896_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L895_burger_annotations.bed.gz -d key=INFO,ID=L895_burger,Number=1,Type=String,Description='L895_burger allele' -c CHROM,FROM,TO,INFO/L895_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L900_burger_annotations.bed.gz -d key=INFO,ID=L900_burger,Number=1,Type=String,Description='L900_burger allele' -c CHROM,FROM,TO,INFO/L900_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L902_burger_annotations.bed.gz -d key=INFO,ID=L902_burger,Number=1,Type=String,Description='L902_burger allele' -c CHROM,FROM,TO,INFO/L902_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L901_burger_annotations.bed.gz -d key=INFO,ID=L901_burger,Number=1,Type=String,Description='L901_burger allele' -c CHROM,FROM,TO,INFO/L901_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L903_burger_annotations.bed.gz -d key=INFO,ID=L903_burger,Number=1,Type=String,Description='L903_burger allele' -c CHROM,FROM,TO,INFO/L903_burger | vcf-annotate -a /scratch/devel/iruiz/Burger_Gorilla/READ/ANNOTATIONS_2/L899_burger_annotations.bed.gz -d key=INFO,ID=L899_burger,Number=1,Type=String,Description='L899_burger allele' -c CHROM,FROM,TO,INFO/L899_burger | python infotogenotype.py | bgzip > downsampling/Gorilla_annotated_downsampling.chr3.vcf.gz 
tabix -p vcf downsampling/Gorilla_annotated_downsampling.chr3.vcf.gz
