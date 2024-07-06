import json
import numpy as np
import string
import re
from sklearn.pipeline import Pipeline
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

with open(sys.argv[1], 'r', encoding='utf-8') as fp:
        train_data = json.load(fp)
        
train_X = []
train_labels = []

for i in range(len(train_data)):
    train_X.append(train_data[i]['text'])
    train_labels.append(train_data[i]['langid'])
    
train_X = np.array(train_X)
train_labels = np.array(train_labels)

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
    
for i in range(len(train_X)):
    train_X[i] = text_processing(train_X[i])
    

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(ngram_range=(1, 2))),
    ('classifier', MultinomialNB(alpha=0.0001, force_alpha=True, fit_prior=True, class_prior=None))
])

pipeline.fit(train_X, train_labels)

import joblib
joblib.dump(pipeline, sys.argv[2])





