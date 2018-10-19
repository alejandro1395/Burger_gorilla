import fileinput

ancientsamples=['L894_burger','L895_burger','L896_burger','L897_burger','L898_burger','L899_burger','L900_burger','L901_burger','L902_burger','L903_burger','L904_burger']

for line in fileinput.input():
    line=line.strip()
    if line.startswith("#"):
        if line.startswith("#CHROM"):
            ele=line.split()
            ele=ele+ancientsamples
            print "\t".join(ele)
            continue
        print line
        continue
    ele=line.split()
    #['scaffold1', '518', '.', 'A', 'G', '943.37', '.', 'DP=89;MLEAC=4;MLEAF=0.200;MQ=60.00;CAVE=A', 'GT:AD:DP:GQ:PL'
    info=ele[7]
    ref=ele[3]
    alt=ele[4]
    ancient=[x for x in ele[7].split(";") if x.split("=")[0] in ancientsamples]
    ancienti=[x.split("=")[0] for x in ancient]
    ngt=[]

    for aindiv in ancientsamples:
        if aindiv not in ancienti:
            ngt.append("./.")
            continue
        acave=[x.split("=")[1] for x in ancient if aindiv in x][0]
        if acave==ref:
            ngt.append("0/0")
        if acave==alt:
            ngt.append("1/1")
        if acave!=alt and acave!=ref and acave!="N":
            ngt.append("2/2")
        if acave=="N":
            ngt.append("./.")

    ele=ele+ngt
    print "\t".join(ele)
