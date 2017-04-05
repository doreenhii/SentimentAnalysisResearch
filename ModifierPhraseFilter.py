import string
import re
data_files = ["SA_imdb_labelled.txt", "SA_yelp_labelled.txt", "SA_amazon_labelled.txt"]
correct_files = ["correct_SA_imdb_labelled.txt","correct_SA_yelp_labelled.txt","correct_SA_amazon_labelled.txt"]
wrong_files = ["wrong_SA_imdb_labelled.txt","wrong_SA_yelp_labelled.txt","wrong_SA_amazon_labelled.txt"]

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

negators = getLines("negators_fixed.txt")
flag_word_set = negators[0].split("\t")

for i in range(3):
	data = getLines("ProcessedData/" + correct_files[i])
	pulled_out_data = open("ProcessedData/pulled_out_" + correct_files[i],"wb")

	for line in data:
		words = line.split("\t")
		words = words[0].translate(None, string.punctuation).split(" ")
		words = filter(lambda a: a != '', words)
		#print(words)
		for word in words:
			for flag in flag_word_set:
				if(word.lower() == flag.lower()):
					pulled_out_data.write(line)
					break

	data = getLines("ProcessedData/" + wrong_files[i])
	pulled_out_data = open("ProcessedData/pulled_out_" + wrong_files[i],"wb")

	for line in data:
		words = line.split("\t")
		words = words[0].translate(None, string.punctuation).split(" ")
		words = filter(lambda a: a != '', words)
		#print(words)
		for word in words:
			for flag in flag_word_set:
				if(word.lower() == flag.lower()):
					pulled_out_data.write(line)
					break



#print(str(point_one_count) + "/" + str(total))