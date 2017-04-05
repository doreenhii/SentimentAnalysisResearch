data_files = ["SA_imdb_labelled.txt", "SA_yelp_labelled.txt", "SA_amazon_labelled.txt"]
correct_files = ["correct_"+data_files[0],"correct_"+data_files[1],"correct_"+data_files[2]]
wrong_files = ["wrong_"+data_files[0],"wrong_"+data_files[1],"wrong_"+data_files[2]]

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

data = getLines(data_files[0])
correct_data = open(correct_files[0],"wb")
wrong_data = open(wrong_files[0],"wb")

split_correct_data = []
split_wrong_data = []

for line in data:
	words = line.split("\t")
	if(float(words[1]) > 0 and float(words[2]) < 0) or (float(words[1]) < 0 and float(words[2]) > 0) or (float(words[2]) == 0 or float(words[2]) == 0.1):
		split_wrong_data.append(words)
	else:
		split_correct_data.append(words)

split_correct_data.sort(key=lambda x: x[4], reverse= True)
split_wrong_data.sort(key=lambda x: x[4], reverse= True)

point_one_count = 0
total = 0

for line in split_wrong_data:
	wrong_data.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + line[4])

for line in split_correct_data:
	correct_data.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + line[4])

#print(str(point_one_count) + "/" + str(total))