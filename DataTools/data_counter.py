def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

print "Correct Sentences w/ negators: {} vs Wrong Sentences w/ negators {}".format(len(getLines("pulled_out_correct_imdb_labelled.txt")),len(getLines("pulled_out_wrong_imdb_labelled.txt")))
