#!usr/bin/env python3

# Calculates the mean and standard deviation of all individuals


import pprint
import statistics

def main():
	infile = open("/stor/work/Ochman/yli19/raw_data/20190919_aphidReseqHiSeq2500/JA18299-87128041/pea_aphid_coverage_region", "r")
	my_list3 = []
	my_list4 = []
	my_list5 = []
	my_list6 = []
	my_list7 = []
	my_list8 = []
	my_list9 = []

	for line in infile:
		line = line.strip()
		line = line.split("\t")

		my_list3.append(int(line[3]))
		my_list6.append(int(line[6]))
		my_list9.append(int(line[9]))

		my_list4.append(int(line[4]))
		my_list5.append(int(line[5]))
		my_list7.append(int(line[7]))
		my_list8.append(int(line[8]))


	infile.close()
	print("Col 3", statistics.mean(my_list3), statistics.stdev(my_list3))
	print("Col 6", statistics.mean(my_list6), statistics.stdev(my_list6))
	print("Col 9", statistics.mean(my_list9), statistics.stdev(my_list9))

	print("Col 4", statistics.mean(my_list4), statistics.stdev(my_list4))
	print("Col 5", statistics.mean(my_list5), statistics.stdev(my_list5))
	print("Col 7", statistics.mean(my_list7), statistics.stdev(my_list7))
	print("Col 8", statistics.mean(my_list8), statistics.stdev(my_list8))


if __name__ == "__main__":
	main()