#!usr/bin/env python3

# depth_vs_ratio

import statistics
import matplotlib.pyplot as plt

def main():
	avg_cov = {}

	infile = open("./pea_aphid_22Mar2018_4r6ur.genome", "r")
	for line in infile:
		line = line.strip()
		line = line.split("\t")
		avg_cov[line[0]] = int(line[1])

	by_scaffold = {}
	infile2 = open("./pea_aphid_coverage_region", "r")
	for line in infile2:
		if "Scaffold_21967;HRSCAF=25451" in line or "Scaffold_21646;HRSCAF=24477" in line or "Scaffold_20849;HRSCAF=22316" in line or "Scaffold_21773;HRSCAF=24826" in line:
			continue
		else:
			line = line.strip()
			line = line.split("\t")
			scaffold_name = line[0]
			scaffold_length = avg_cov[scaffold_name]

			# Numbers for female individuals
			# Num1 (Col 3) is for AL4f; we are normalizing to it
			num1, num2, num3 = int(line[3]), int(line[6]), int(line[9])
			num2 = num2 / 3840.1422664544907 * 5254.781893755598
			num3 = num3 / 8737.55718310594 * 5254.781893755598

			# Take median coverage for female
			med1 = statistics.median([num1, num2, num3])

			# Numbers for male individuals
			# Num7 (Col 8) is for AL4mw-B; we are normalizing to it
			num4, num5, num6, num7 = int(line[4]), int(line[5]), int(line[7]), int(line[8])
			num4 = num4 / 3551.8488117287975 * 4987.9331124618475 
			num5 = num5 / 3650.0340655136133 * 4987.9331124618475 
			num6 = num6 / 2677.3689249471736 * 4987.9331124618475 

			# Take median coverage for male
			med2 = statistics.median([num4, num5, num6, num7])

			# Ratio between two medians, male / female, is calculated
			ratio = med2 / med1
			if scaffold_name not in by_scaffold:
				by_scaffold[scaffold_name] = [ratio]
			else:
				by_scaffold[scaffold_name].append(ratio)

	infile2.close()
	X, Y = [], []
	for key in by_scaffold:
		total = 0
		for item in by_scaffold[key]:
			total += item
		total = total / len(by_scaffold[key])
		X.append(avg_cov[key])
		Y.append(total)

	plt.scatter(X, Y, color="g")

	plt.xlabel("Length of Scaffold", fontsize=16)
	plt.ylabel("Ratio of Coverage (Male / Femal)", fontsize=16)
	plt.title("Miscellaneous Scaffolds", fontsize=20)
	plt.show()

	

if __name__ == "__main__":
	main()