


def main():
	infile = open("./AL4m-C_S5_L001_R1_001_depth.txt", "r")

	num_position = 119541756
	total = 0

	for line in infile:
		line = line.strip()
		line = line.split("\t")
		try:
			read = line[2]
			total += int(read)
		except IndexError:
			read = 0

	avg_read_depth = total / num_position
	print(avg_read_depth)

if __name__ == "__main__":
	main()