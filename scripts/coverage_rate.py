#!usr/bin/env python3

# Calculates coverage rate

def main():
	infile = open("/stor/work/Ochman/yli19/raw_data/20190919_aphidReseqHiSeq2500/JA18299-87128041/pea_aphid_coverage", "r")
	num_line = 0
	my_list = [0, 0, 0, 0, 0, 0, 0]

	for line in infile:
		num_line += 1
		line = line.strip()
		line = line.split("\t")
		if line[3] == "0":
			my_list[0] += 1
		if line[4] == "0":
			my_list[1] += 1
		if line[5] == "0":
			my_list[2] += 1
		if line[6] == "0":
			my_list[3] += 1
		if line[7] == "0":
			my_list[4] += 1
		if line[8] == "0":
			my_list[5] += 1
		if line[9] == "0":
			my_list[6] += 1

	infile.close()
	new_list = []

	for i in my_list:
		new_list.append(i/num_line)
	print(my_list)

if __name__ == "__main__":
	main()