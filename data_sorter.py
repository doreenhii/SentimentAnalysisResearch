with open("SCL-OPP_stanford_analyzed_data.txt") as f:
	data = f.readlines()

split_data = []
for line in data:
	words = line.split("\t")
	split_data.append(words)

split_data.sort(key=lambda x: x[1], reverse= True)
print(split_data)

analyzed_data = open("SCL-OPP_stanford_analyzed_polar_data_sorted.txt","wb")
point_one_count = 0
total = 0
for line in split_data:
	if(float(line[2]) < 0 and float(line[3]) > 0) or (float(line[2]) > 0 and float(line[3]) < 0):
		"""if(float(line[2]) == 0.1):
			point_one_count += 1
		total += 1"""
		analyzed_data.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3])

#print(str(point_one_count) + "/" + str(total))