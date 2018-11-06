#!usr/bin/env python3

import pprint
import statistics

def main():
	infile = open("/stor/work/Ochman/yli19/raw_data/20190919_aphidReseqHiSeq2500/JA18299-87128041/pea_aphid_coverage", "r")
	my_list = []
	outstring = ""

	num_line = 0
	out_line = 0

	for line in infile:
		num_line += 1
		linestring = line
		line = line.strip()
		line = line.split("\t")
		num = int(line[3])
		if num > 2252 and num < 7400:
			outstring += linestring
			out_line += 1

	infile.close()
	print(num_line, out_line)

	outfile = open("/stor/work/Ochman/yli19/raw_data/20190919_aphidReseqHiSeq2500/JA18299-87128041/pea_aphid_coverage_region", "w")
	outfile.write(outstring)
	outfile.close()

if __name__ == "__main__":
	main()