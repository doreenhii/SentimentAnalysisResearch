def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data

correct = len(getLines("ProcessedData/pulled_out_correct_SA_imdb_labelled.txt"))
wrong = len(getLines("ProcessedData/pulled_out_wrong_SA_imdb_labelled.txt"))
print "IMDB: Correct Sentences w/ negators: {} vs Wrong Sentences w/ negators {}: %{}".format(correct, wrong, wrong*100/float(correct+wrong))
correct = len(getLines("ProcessedData/pulled_out_correct_SA_amazon_labelled.txt"))
wrong = len(getLines("ProcessedData/pulled_out_wrong_SA_amazon_labelled.txt"))
print "Amazon: Correct Sentences w/ negators: {} vs Wrong Sentences w/ negators {}: %{}".format(correct, wrong, wrong*100/float(correct+wrong))
correct = len(getLines("ProcessedData/pulled_out_correct_SA_yelp_labelled.txt"))
wrong = len(getLines("ProcessedData/pulled_out_wrong_SA_yelp_labelled.txt"))
print "Yelp: Correct Sentences w/ negators: {} vs Wrong Sentences w/ negators {}: %{}".format(correct, wrong, wrong*100/float(correct+wrong))

#IMDB: Correct Sentences w/ negators: 124 vs Wrong Sentences w/ negators 21: %14.4827586207
#Amazon: Correct Sentences w/ negators: 141 vs Wrong Sentences w/ negators 15: %9.61538461538
#Yelp: Correct Sentences w/ negators: 154 vs Wrong Sentences w/ negators 23: %12.9943502825