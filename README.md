# Language Identification
## Problem Statement:
The motivation of this assignment is to get the students some practice with text categorization using machine learning. We do this for language identification, which is a crucial step for various natural language processing tasks such as machine translation, sentiment analysis, and information retrieval.
You must develop a classifier that inputs a text in Roman script and outputs the language in which the text is written. We provide the supervised dataset in JSON format for building this classifier.
* train.json and valid.json contain training and validation data, respectively. The files use UTF-8 encoding.
* The train and test data consist of about 800k and 100k samples, respectively. Each sample is a dictionary as given below
````
"text": "esto es español",
"langid": "es"
````
* The data consists of text from 13 different languages. Text within each sample is written in a single dominant script, i.e., the Roman script.
