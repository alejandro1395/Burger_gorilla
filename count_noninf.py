#!/usr/bin/python3

import sys
import re
import gzip

if len(sys.argv) == 2:
    vcf_file = sys.argv[1]
else:
    sys.exit("The usage should be ./irune.py vcf_file")

#Variables
species_names = []
total_count = 0
dc_list = []
dict_count = {}
start_of_SNPs = False

#FUNCTIONS


#Now we open the vcf file

with gzip.open(vcf_file, "rt") as f:
    for line in f:
        line.rstrip()
        if line.startswith("#CHROM"):
            fields = line.split("\t")
            for i in range(9, len(fields)):
                name_species = fields[i].rstrip()
                species_names.append(name_species)
            for m in range(0, len(species_names)):
                for n in range(m+1, len(species_names)):
                    dict_count[species_names[m]+species_names[n]] = 0
            start_of_SNPs = True
        else:
            if start_of_SNPs is True:
                fields_snp = line.split("\t")
                count = 0
                for m in range(52, len(fields_snp)):
                    alleles = fields_snp[m].split("/")
                    if (str(0) or str(1)) in alleles:
                        count += 1
                if count == 1:
                    print(count)
                    total_count += 1

    print(total_count)
