#!usr/bin/env python3

import statistics
import matplotlib.pyplot as plt

def main():
	infile = open("./pea_aphid_coverage_region", "r")
	ratio_list = []

	for line in infile:
		if "Scaffold_21646;HRSCAF=24477" in line:
		#"Scaffold_21967;HRSCAF=25451" in line or "Scaffold_21646;HRSCAF=24477" in line or "Scaffold_20849;HRSCAF=22316" in line:
		#or "Scaffold_21773;HRSCAF=24826" in line:
		# X chromosome: "Scaffold_21773;HRSCAF=24826" in line:
		# Autosomes: "Scaffold_21646;HRSCAF=24477" in line or "Scaffold_20849;HRSCAF=22316" in line or "Scaffold_21773;HRSCAF=24826" in line:
			line = line.strip()
			line = line.split("\t")

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
			ratio_list.append(ratio)

	# Draw histogram with matplotlib
	print(statistics.mean(ratio_list), statistics.stdev(ratio_list))
	f = plt.figure()
	plt.hist(ratio_list, density=False, bins=1500)
	plt.axis([0.25, 1.75, 0, 2500])
	plt.title("Chromosome 3")
	plt.xlabel("Ratio of Coverage (Male/Female) (bin size = 0.01)")
	plt.ylabel("Count")
	plt.show()

	# How to save figure in PDF format: https://stackoverflow.com/questions/11328958/save-the-plots-into-a-pdf
	f.savefig("foo_3.pdf", bbox_inches = "tight")

	infile.close()

if __name__ == "__main__":
	main()

