import string
import re
data_files = ["SA_imdb_labelled.txt", "SA_yelp_labelled.txt", "SA_amazon_labelled.txt"]
correct_files = ["correct_"+data_files[0],"correct_"+data_files[1],"correct_"+data_files[2]]
wrong_files = ["wrong_"+data_files[0],"wrong_"+data_files[1],"wrong_"+data_files[2]]

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

data = getLines("correct_SA_imdb_labelled.txt")
pulled_out_data = open("pulled_out_correct_imdb_labelled.txt","wb")

negators = getLines("negators_fixed.txt")
flag_word_set = negators[0].split("\t")
#flag_word_set = ['problem', 'exceptional']

for line in data:
	words = line.split("\t")
	words = words[0].translate(None, string.punctuation)
	words = words.split(" ")
	words = filter(lambda a: a != '', words)
	print(words)
	for word in words:
		for flag in flag_word_set:
			if(word.lower() == flag.lower()):
				pulled_out_data.write(line)
				break


#print(str(point_one_count) + "/" + str(total))