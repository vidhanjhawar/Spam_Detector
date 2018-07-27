from nltk.stem.snowball import SnowballStemmer
import string
import pickle
import pandas as pd
from nltk.corpus import stopwords
from unicodedata import category

#function for stemming text list
def steming(text_input):
	text_output=[]
	stemmer = SnowballStemmer('english',ignore_stopwords=True)
	word_list = text_input.split()
	stop_words=set(stopwords.words('english'))
	
	#Removing stopwords from text list
	for j in word_list:
		if j not in stop_words:
			text_output.append(stemmer.stem(j))
	
	text_output = ' '.join(text_output)
	
	return text_output

def parseOutText(f):
	prep=[]
	for i in range(0,len(f)):
		# remove punctuation
		text_string = "".join(ch for ch in f[i] if category(ch)[0]!= 'P')
		words = steming(text_string)
		prep.append(words)    
	return prep
