#!usr/bin/env python3

import pprint

def main():
	chr1 = "Scaffold_20849;HRSCAF=22316"
	chr2 = "Scaffold_21967;HRSCAF=25451"
	chr3 = "Scaffold_21646;HRSCAF=24477"
	chrX = "Scaffold_21773;HRSCAF=24826"

	HOMO = {chr1:[0, 0, 0, 0, 0, 0, 0], chr2:[0, 0, 0, 0, 0, 0, 0], chr3:[0, 0, 0, 0, 0, 0, 0], chrX:[0, 0, 0, 0, 0, 0, 0]}
	HETERO = {chr1:[0, 0, 0, 0, 0, 0, 0], chr2:[0, 0, 0, 0, 0, 0, 0], chr3:[0, 0, 0, 0, 0, 0, 0], chrX:[0, 0, 0, 0, 0, 0, 0]}

	infile = open("/stor/work/Ochman/hyunjin/freebayes_filtering/SNP.bed", "r")
	outstring = ""
	for line in infile:
		if line[0] != "#":
			line = line.strip()
			line = line.split()
			# Test of heterozygous SNP of AL4f
			if line[-1][:3] == "0/1" or line[-1][:3] == "1/0":
				outline = line[0] + "\t" + line[1] + "\t" + line[2] + "\n"
				outstring += outline

	outfile = open("SNP_AL4f.bed", "w")
	outfile.write(outstring)
	outfile.close()

if __name__ == "__main__":
	main()

# python3 /stor/work/Ochman/hyunjin/data/genomes/dovetail/python_scripts/SNP_individual.py

"""
bedtools intersect -a /stor/work/Ochman/hyunjin/data/genomes/dovetail/pea_aphid_10kb_2kb.bed -b /stor/work/Ochman/hyunjin/freebayes_filtering/SNP_AL4f.bed -c > SNP_AL4f_windows.bed

awk '{ if (($4 >= 0) && ($4 < 6)) {print} }' SNP_AL4f_windows.bed | wc -l
0-5:	160838
6-10:	34343
11-15:	31270
16-20:	24401
21-25:	16291
26-30:	8970
31-35:	4246
36-40:	1701
41-45:	621
46-50:	208
51-55:	39
56-60:	8
61-:	0


"""