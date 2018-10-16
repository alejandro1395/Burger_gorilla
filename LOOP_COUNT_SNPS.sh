#!/usr/bin/bash

#Iterate over samples and retrieve SNP count

echo {10..19} | tr " " "\n" | while read column; do zcat /scratch/devel/iruiz/Burger_Gorilla/DOWNSAMPLING/Gorilla_burger_freebayes_downsampling.vcf.gz \
 | tail -n+57 | cut -f $column | cut -d ":" -f 1 | sort | uniq -c >  downsampling_count_${column}.txt ; done
