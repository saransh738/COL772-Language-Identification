import sys
import joblib
import json
import numpy as np
import string
import re
from sklearn.pipeline import Pipeline
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

with open(sys.argv[2], 'r', encoding='utf-8') as fp:
        valid_data = json.load(fp)
        
test_X = []
test_labels = []
    
for i in range(len(valid_data)):
    test_X.append(valid_data[i]['text'])
    test_labels.append(valid_data[i]['langid']) 
    
test_X = np.array(test_X)
test_labels = np.array(test_labels)

def text_processing(text):
    punctuations = string.punctuation
    text = ''.join(char for char in text if char not in punctuations)
    re.sub(r'\d+', ' ', text)
    re.sub(r'[^\w\s]', ' ', text)
    re.sub(r'-', ' ', text)
    re.sub(r'\s', '_', text)
    stopwords = ['the', 'and', 'is', 'in', 'of', 'it', 'to', 'a', 'for', 'on', 'that', 'with', 'as', 'at']
    lower_text = text.lower()
    words = lower_text.split()
    clean_text = [word for word in words if word not in stopwords]
    final_clean_text = ' '.join(clean_text)
    return final_clean_text
    
for i in range(len(test_X)):
    test_X[i] = text_processing(test_X[i])

pipeline = joblib.load(sys.argv[1])
preds = pipeline.predict(test_X)

with open(sys.argv[3], 'w') as f:
    for row in preds:
        f.write(row)
        f.write('\n')



