import csv, math
# Imports the Google Cloud client library
from google.cloud import language
# Instantiates a client
language_client = language.Client()

def getLines(file_name):
	with open(file_name) as f:
		data = f.readlines()

	return data
	
def getSentiment(l_client, text):
	document = l_client.document_from_text(text)
	sentiment_value = document.analyze_sentiment().sentiment
	return sentiment_value

#Data Files
data_files = ["imdb_labelled.txt", "yelp_labelled.txt", "amazon_labelled.txt"]
parsed_files = ["SA_"+data_files[0],"SA_"+data_files[1],"SA_"+data_files[2]]

for i in [1,2]:

	data = getLines(data_files[i])
	sentiment_analyzed_data = open(parsed_files[i],"wb")

	for line in data:
		words = line.split("\t") #phrase 
		text = words[0]
		human_rating = float(words[1])

		NLP_value = getSentiment(language_client, text)

		difference = abs(human_rating - NLP_value.score)

		#print('Text: {}'.format(text))
		#print('Predicted Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
		#print('Predicted: {} -- True: {} -- Difference: {}'.format(sentiment.score, human_rating, difference))
		
		sentiment_analyzed_data.write(text + "\t" + str(human_rating) + "\t" + str(NLP_value.score) + "\t" + str(NLP_value.magnitude) + "\t" + str(difference) + "\n")

