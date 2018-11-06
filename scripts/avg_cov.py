#!usr/bin/env python3

import statistics
import matplotlib.pyplot as plt
import pprint

def main():
	infile = open("./bedtools_genomecov_AL4f", "r")
	avg_cov = {}
	Y = []
	X = []

	for line in infile:
		line = line.strip()
		line = line.split("\t")
		scaffold_name = line[0]
		if scaffold_name not in avg_cov:
			# Mean coverage of AL4f is 56.8935; SD, 30.33.
			# The range (7.00065, 106.78635) is obtained by (Mean)+=1.645(SD) to include 90%.
			# The range is rounded to the nearest integer, hence [7, 107]
			if int(line[1]) >= 7 and int(line[1]) <= 107:
				avg_cov[scaffold_name] = int(line[1]) * float(line[4])
		else:
			if int(line[1]) >= 7 and int(line[1]) <= 107:
				avg_cov[scaffold_name] += int(line[1]) * float(line[4])

	infile.close()
	auto_cov = (avg_cov["Scaffold_21967;HRSCAF=25451"] + avg_cov["Scaffold_21646;HRSCAF=24477"] + avg_cov["Scaffold_20849;HRSCAF=22316"]) / 3

	infile2 = open("./pea_aphid_22Mar2018_4r6ur.genome")
	for line in infile2:
		line = line.strip()
		line = line.split("\t")
		scaffold_name = line[0]
		if scaffold_name in avg_cov:
			avg_cov[scaffold_name] = (int(line[1]), avg_cov[scaffold_name])
	avg_cov.pop("genome", None)

	pprint.pprint(avg_cov)
	print(len(avg_cov))

	for key in avg_cov:
		if key not in ["Scaffold_21967;HRSCAF=25451", "Scaffold_21646;HRSCAF=24477", "Scaffold_20849;HRSCAF=22316", "Scaffold_21773;HRSCAF=24826"]:
			x, y = avg_cov[key]
			if x < 250001:
				X.append(x)
				Y.append(y)
			else:
				print(key, x, y)

	plt.scatter(X, Y, color="r")

	plt.xlabel("Length of Scaffold", fontsize=16)
	plt.ylabel("Average Depth of Coverage", fontsize=16)
	plt.title("Miscellaneous Scaffolds", fontsize=20)
	plt.hlines(auto_cov, xmin = 0, xmax = max(X))
	plt.show()
	print("Avg autosome depth:", auto_cov)

	infile.close()

if __name__ == "__main__":
	main()