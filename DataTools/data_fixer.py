with open("amazon_labelled.txt") as f:
	data = f.readlines()

split_data = []
for line in data:
	words = line.split("\t")
	split_data.append(words)

analyzed_data = open("amazon_labelled.txt","wb")

for line in split_data:
	value = int(line[1])
	if(value == 0):
		value = -1
	print(value)
	analyzed_data.write(line[0] + "\t" + str(value) + "\n")

#print(str(point_one_count) + "/" + str(total))