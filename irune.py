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



#Then we iterate in order to count the number of shared alleles

#VARIABLES

#Genotypes_subj_1 = {}
#Genotypes_subj_2 = {}
#Genotypes_subj_3 = {}
#Genotypes_fam_4 = {}
#...
#List_dict = [Genotypes_subj1, 2, etc]
#CREAD DICCIONARIOS PARA CADA INDIVIDUO Y UNA LISTA QUE CONTENGA LOS DICCIOANRIOS COMO ELEMENTOS


# Guardar en un diccionario los genotipos para cada SNP de los distintos individuos

#with open(seq_fasta, "r") as in_fh:
  #for line in in_fh:
    #line = line.rstrip()
    #if not line.startswith("#"):
      #fields = line.split("\t")
      #Genotypes_subj1[fields[0]] = fields[8]--> FIelds0 es el SNP (key del diccionario) y el 8es la columna donde esta el genotipo 0|0 o 0|1 de ese sujeto. Lo suyo seria
      #que el genotipo estuviera en forma de lista con 2 elementos , los dos alelos.
      #Genotypes_subj2[fields[0]] = fields[9]
      #... -> asi para  todos los sujetos


#POR ULTIMO ITERAS LOS ELEMENTOS DE LA LISTA PARA TENER TODAS LAS COMBINACIONES DE INDIVIDUOS Y SACAR SU KINSHIP

# for i in range(len(List_dict)):
  # for j in range(i+1, len(List_dict)):
    # for key in List_dict[i]:
      # if List_dict[i][key] == List_dict[j][key] or List_dict[i][key] == rev(List_dict[j][key]): --> ESTO COMPARA LOS GENOTIPOS DE CADA SNP DE CADA DOS INDIVIDUOS EN LOOP
        # comparten los dos alelos para ese SNP ( puedes poner un contador que sume +2 indicativo)
      #elif List_dict[i][key][0] in List_dict[j][key] AND NOT List_dict[i][key][1] in List_dict[j][key]:
        # comparten solo 1 alelos (+1)
      #else:
        #NO COMPARTEN ALELOS PARA ESE SNP (+0)

#puedes hacer un contador para cada pareja de individuos y al final tendras un indicio de cuantos alelos comparten todos entre todos!
