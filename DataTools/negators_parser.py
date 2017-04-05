import string
import re
data_files = ["SA_imdb_labelled.txt", "SA_yelp_labelled.txt", "SA_amazon_labelled.txt"]
correct_files = ["correct_"+data_files[0],"correct_"+data_files[1],"correct_"+data_files[2]]
wrong_files = ["wrong_"+data_files[0],"wrong_"+data_files[1],"wrong_"+data_files[2]]

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

negators = getLines("negators.txt")
negators_fixed = open("negators_fixed.txt","wb")
negators_list = []
for i in range((len(negators)/4)+1):
	fixed_word = negators[i*4].split("#")[0].strip('\n')
	negators_fixed.write(fixed_word+"\t")
	negators_list.append(fixed_word)
print negators_list
print(len(negators_list))
"""
for line in data:
	words = line.split("\t")
	words = words[0].translate(None, string.punctuation)
	words = words.split(" ")
	words = filter(lambda a: a != '', words)
	print(words)
	for word in words:
		for flag in flag_word_set:
			if(word == flag):
				pulled_out_data.write(line)
				break
"""


#print(str(point_one_count) + "/" + str(total))