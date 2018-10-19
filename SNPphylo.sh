#!/bin/bash

#SET DIRECTORIES
IN="/scratch/devel/iruiz/Burger_Gorilla/KING/hg19/VCF_hg19_2/"
OUTDIR="/scratch/devel/avalenzu/Burger_gorilla/SNPphylo/"

#SET OUTPUT
out=${OUTDIR}"out/"
qu=${OUTDIR}"qu/"
jobname=${qu}"SNPphylo.sh"

#CREATE THIS DIRECTORIES

mkdir -p $OUTDIR
mkdir -p $out
mkdir -p $qu

#MAIN JOB

echo "#!/bin/bash
/scratch/devel/avalenzu/Burger_gorilla/bin/SNPhylo/snphylo.sh -v ${IN}Gorilla_burger_filtered_hg19.vcf.gz -p 80 -c 0 -H ${OUTDIR}/HapMap_file -s ${OUTDIR}/Simple_SNP_file -d ${OUTDIR}/GDS_file -P \
out_file -b -A" >> ${jobname}

chmod 755 ${jobname}
/scratch/devel/avalenzu/CNAG_interface/submit.py -c ${jobname} -n pipeline_SNPphylo -o ${out}snps.out -e ${out}snps.err -u 1 -t 1 -w "05:00:00"
