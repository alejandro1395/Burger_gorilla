#!/usr/bin/python3

import sys
import re
import gzip

if len(sys.argv) == 3:
    vcf_file = sys.argv[1]
    out_file = sys.argv[2]
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

with gzip.open(vcf_file, "rt") as f, open(out_file, "w") as out_fh:
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
                total_count += 1
                for m in range(9, len(fields_snp)):
                    for n in range(m+1, len(fields_snp)):
                        alleles_1 = fields_snp[m].split(":")[0].split("/")
                        alleles_2 = fields_snp[n].split(":")[0].split("/")
                        if "." in (alleles_1 or alleles_2):
                            continue
                        if set(alleles_1) == set(alleles_2):
                            dict_count[species_names[m-9]+species_names[n-9]] += 2
                            #print(dc_list[m][species_names[m]][snp_key], dc_list[n][species_names[n]][snp_key])
                        elif any(number in alleles_2 for number in alleles_1):
                            dict_count[species_names[m-9]+species_names[n-9]] += 1
                        else:
                            dict_count[species_names[m-9]+species_names[n-9]] += 0
    dict_count = {k: v / (total_count * 2) for k, v in dict_count.items()}
    print(dict_count, file=out_fh)
