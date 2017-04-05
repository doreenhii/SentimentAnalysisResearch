data_files = ["ProcessedData/SA_imdb_labelled.txt", "ProcessedData/SA_yelp_labelled.txt", "ProcessedData/SA_amazon_labelled.txt"]
correct_files = ["ProcessedData/correct_SA_imdb_labelled.txt","ProcessedData/correct_SA_yelp_labelled.txt","ProcessedData/correct_SA_amazon_labelled.txt"]
wrong_files = ["ProcessedData/wrong_SA_imdb_labelled.txt","ProcessedData/wrong_SA_yelp_labelled.txt","ProcessedData/wrong_SA_amazon_labelled.txt"]

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

data = getLines(data_files[2])
correct_data = open(correct_files[2],"wb")
wrong_data = open(wrong_files[2],"wb")

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