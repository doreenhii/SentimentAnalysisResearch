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
	l_client.document_from_text(text)
	sentiment_value = document.analyze_sentiment().sentiment
	return sentiment_value

data = getLines("")

for line in data:
	words = line.split("\t") #phrase 
	text = words[0]
	human_rating = float(words[1])

	document = language_client.document_from_text(text)
	# Detects the sentiment of the text
	sentiment = document.analyze_sentiment().sentiment

	difference = abs(sentiment.score - human_rating)

	print('Text: {}'.format(text))
	#print('Predicted Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
	print('Predicted: {} -- True: {} -- Difference: {}'.format(sentiment.score, human_rating, difference))
	
	analyzed_data.write(text + "\t" + str(difference) + "\t" + str(sentiment.score) + "\t" + str(sentiment.magnitude) + "\t" + str(human_rating) + "\n")

