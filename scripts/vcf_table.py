#!usr/bin/env python3

import pprint

def main():
	chr1 = "Scaffold_20849;HRSCAF=22316"
	chr2 = "Scaffold_21967;HRSCAF=25451"
	chr3 = "Scaffold_21646;HRSCAF=24477"
	chrX = "Scaffold_21773;HRSCAF=24826"

	HOMO = {chr1:[0, 0, 0, 0, 0, 0, 0], chr2:[0, 0, 0, 0, 0, 0, 0], chr3:[0, 0, 0, 0, 0, 0, 0], chrX:[0, 0, 0, 0, 0, 0, 0]}
	HETERO = {chr1:[0, 0, 0, 0, 0, 0, 0], chr2:[0, 0, 0, 0, 0, 0, 0], chr3:[0, 0, 0, 0, 0, 0, 0], chrX:[0, 0, 0, 0, 0, 0, 0]}

	infile = open("/stor/work/Ochman/hyunjin/freebayes_filtering/freebayes_parallel_attempt4_qual20-AB-MQM-DP-prim-removehighdepth-SNP.vcf", "r")
	
	for line in infile:
		if line[0] != "#":
			line = line.strip()
			line = line.split()
			if chr1 in line[0]:
				genotype = []
				for i in range(9, 16):
					genotype.append(line[i][:3])
				for j in range(len(genotype)):
					if genotype[j] == "1/1":
						HOMO[chr1][j] += 1
					elif genotype[j] == "0/1" or genotype[j] == "1/0":
						HETERO[chr1][j] += 1
			elif chr2 in line[0]:
				genotype = []
				for i in range(9, 16):
					genotype.append(line[i][:3])
				for j in range(len(genotype)):
					if genotype[j] == "1/1":
						HOMO[chr2][j] += 1
					elif genotype[j] == "0/1" or genotype[j] == "1/0":
						HETERO[chr2][j] += 1
			elif chr3 in line[0]:
				genotype = []
				for i in range(9, 16):
					genotype.append(line[i][:3])
				for j in range(len(genotype)):
					if genotype[j] == "1/1":
						HOMO[chr3][j] += 1
					elif genotype[j] == "0/1" or genotype[j] == "1/0":
						HETERO[chr3][j] += 1
			elif chrX in line[0]:
				genotype = []
				for i in range(9, 16):
					genotype.append(line[i][:3])
				for j in range(len(genotype)):
					if genotype[j] == "1/1":
						HOMO[chrX][j] += 1
					elif genotype[j] == "0/1" or genotype[j] == "1/0":
						HETERO[chrX][j] += 1
	print("HOME")
	pprint.pprint(HOMO)
	print()
	print("HETERO")
	pprint.pprint(HETERO)

if __name__ == "__main__":
	main()