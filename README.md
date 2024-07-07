# Language Identification
## Problem Statement:
The motivation of this assignment is to get the students some practice with text categorization using machine learning. We do this for language identification, which is a crucial step for various natural language processing tasks such as machine translation, sentiment analysis, and information retrieval.
The goal is to develop a classifier that inputs a text in Roman script and outputs the language in which the text is written. The supervised dataset is in JSON format for building this classifier.
* train.json and valid.json contain training and validation data, respectively. The files use UTF-8 encoding.
* The train and test data consist of about 800k and 100k samples, respectively. Each sample is a dictionary as given below
````
"text": "esto es español",
"langid": "es"
````
* The data consists of text from 13 different languages. Text within each sample is written in a single dominant script, i.e., the Roman script.

## Approach:
In this assignment, we will explore non-neural techniques for classification like Naïve Bayes, Logistic Regression, SVMs, Random Forests, etc. We can start by building a baseline using any of these models with unigrams as features. We recommend that you thoroughly review the data, build new features that you think are best for this problem, and improve over the baseline. We provide a few suggestions below.
* We have provided a training and validation split of the training data. You don’t have to use this specific split. You can do anything you wish with this data (including resplitting to create a test set, etc)
* Explore different balancing strategies to handle class imbalance.
* Experiments with different regularisation strategies for your model. For instance, you can consider  L2-regularization for Logistic Regression.
* Besides unigrams, you can consider bi-gram and tri-gram features. On the other end, you can explore sub-word-level features, too.
* Consider working with the features by using techniques such as removal of stop words and infrequent words, and TF-IDF weighting.
* Design regular expressions to identify characteristic patterns in the samples and use them as features.
* Using trained word embeddings or neural models or any method that uses neural models is strictly prohibited.
* Perform a good hype-parameter search and select the ones that work the best.
* Explore strategies like One v/s One, One v/s All for Multiclass classification.

## Evaluation Metric:
We will assess the predictive power of submission using the MicroF1 and MacroF1 scores. For this assignment, we compute MicroF1 and MacroF1 on the test set as follows
* We initialize counts for true positive (TP), false positive (FP) and false negative (FN) to zero.
* For a test text written in English, we increment the FP and FN by 1 if the submission makes a mistake.
* For a test text written in a language other than English, we increment TP by 1 if the submission identifies the language correctly. Otherwise, we increment both FP and FN by 1.
We compute Precision, Recall and F1 using TP, FP and FN counts. Observe that our MicroF1 has a special treatment for English differently. Similarly, we compute these values for each language (other than English) to compute Macro F1.

## Usage:
### Using run.sh
The command to train the model is
````
bash run_model.sh train <path_to_data_json> <path_to_save>
````
This command should save the trained model using the data given at location path_to_data_json. Further, it must save the trained model and other necessary files in the path_to_save directory.

The command to run inference using the model is
````
bash run_model.sh test <path_to_save> <path_to_test_json> output.txt
````
This command loads the model saved in path_to_save and predicts the language for each sample from the JSON file located at path_to_test_json. Further, it must store the predicted languages in output.txt. Each line in output.txt should include language IDs corresponding to each sample in the test data.
