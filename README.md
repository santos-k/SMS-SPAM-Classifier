# SMS/Email Spam Classification

![img_1.png](img_1.png)


[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Dash 2.7](https://img.shields.io/badge/Dash-2.7-blue)](https://dash.plotly.com/)
[![Plolty 5.11](https://img.shields.io/badge/Plotly-5.11-blue)](https://pypi.org/project/plotly/)
![GitHub repo size](https://img.shields.io/github/repo-size/santos-k/SMS-SPAM-Classifier?logo=github) 
![GitHub Repo stars](https://img.shields.io/github/stars/santos-k/SMS-SPAM-Classifier?style=social) 
![GitHub watchers](https://img.shields.io/github/watchers/santos-k/SMS-SPAM-Classifier?style=social) 
![GitHub followers](https://img.shields.io/github/followers/santos-k?style=social) 
![Bower](https://img.shields.io/bower/l/flask) 

This project aimed to train and evaluate a machine learning model for classifying SMS and email messages as spam or not spam. The dataset used for this analysis is the SMS Spam Collection dataset from the UCI Machine Learning Repository, which contains 5,574 SMS messages and labels indicating whether each message is spam or not.

The first step in the project was to preprocess the data by removing duplicate rows, converting the target column to binary values, and performing natural language processing techniques on the message text. The model building process began by trying different machine learning algorithms, starting with Naive Bayes. To make the text data suitable for the model, the text was converted to numerical data using vectorization techniques such as Bag of Words and TF-IDF.

The evaluation metrics used were accuracy, precision, recall, and F1 score. The main focus was on the precision score, as the goal of the model is to minimize the number of false positive predictions (i.e. not spam messages classified as spam). The best results were obtained using the MultinomialNB algorithm, which achieved 95.9% accuracy and 100% precision score.

In conclusion, the MultinomialNB model demonstrated superior performance in classifying SMS and email messages as spam or not spam, as it achieved a precision score of 100%. This suggests that the MultinomialNB model is an effective method for classifying SMS and email messages as spam or not spam and minimizing the number of false positive predictions.


# Analysis Report
This analysis was conducted to classify SMS and email messages as spam or not spam using machine learning techniques. The dataset used for this analysis is the [SMS Spam Collection dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) from the Kaggle, which contains 5,574 SMS messages and labels indicating whether each message is spam or not.

## **Data Exploration**
Upon initial exploration of the dataset, it was found that the dataset contains 5,574 rows and 2 columns. The columns in the dataset are labeled as "v1" and "v2", where "v1" represents the target variable indicating whether the message is spam or not, and "v2" represents the message itself. Upon further exploration, it was found that the dataset is imbalanced, with more not spam messages (ham) than spam messages.

## Data Cleaning
In order to prepare the data for analysis, several data cleaning tasks were performed. Firstly, duplicate rows were removed from the dataset to ensure that each message in the dataset is unique. Secondly, the target column was converted to binary values, where 1 represents a spam message and 0 represents a not spam message.

## Exploratory Data Analysis
Exploratory Data Analysis (EDA) was performed on the cleaned dataset to better understand the characteristics of the spam and not spam messages. Three new features were created to represent the number of characters, words, and sentences in each message. The distributions of these new features were then visualized using histograms and pie charts. The EDA suggested that spam messages tend to have more characters, words, and sentences than not spam messages.

# Model Report
This report details the process of training and evaluating a machine learning model for classifying SMS and email messages as spam or not spam. The dataset used for this analysis is the SMS Spam Collection dataset from the UCI Machine Learning Repository, which contains 5,574 SMS messages and labels indicating whether each message is spam or not.

## Data Preprocessing
The first step in the model building process was to preprocess the data. This included removing duplicate rows, converting the target column to binary values (1 for spam, 0 for not spam), and performing natural language processing techniques on the message text, such as tokenization, removal of special characters, removal of stop words, and stemming.

## Model Building
The model building process began by trying different machine learning algorithms, starting with Naive Bayes. Naive Bayes is known to perform well on textual data, so it was selected as the first algorithm to try.

To make the text data suitable for the model, the text was converted to numerical data using vectorization techniques such as Bag of Words and TF-IDF. The best results were obtained using the BernoulliNB algorithm, which achieved 97% accuracy and 97% precision score. However, this model was found to be predicting not spam messages as spam, which is not desirable.

## Model Evaluation
The evaluation metrics used were accuracy, precision, recall, and F1 score. The main focus was on the precision score, as the goal of the model is to minimize the number of false positive predictions (i.e. not spam messages classified as spam). The BernoulliNB model had a higher accuracy of 97%, but it's not much important in this case as the precision score is also high.

The best results were obtained using the MultinomialNB algorithm, which achieved 95.9% accuracy and 100% precision score. This model correctly identified all not spam messages, minimizing the number of false positive predictions.

## Conclusion
In conclusion, the trained MultinomialNB model demonstrated superior performance in classifying SMS and email messages as spam or not spam, as it achieved a precision score of 100%. This suggests that the MultinomialNB model is an effective method for classifying SMS and email messages as spam or not spam and minimizing the number of false positive predictions. The BernoulliNB model had a higher accuracy, but it's not much important in this case as the precision score is also high.



![image](https://user-images.githubusercontent.com/40932902/168224057-d1391cf8-f9ef-4d37-9a8b-25d9d7cdeb80.png)
![image](https://user-images.githubusercontent.com/40932902/168224199-f36dfa2e-8f23-4309-b604-be9ce3db65c8.png)
![image](https://user-images.githubusercontent.com/40932902/168224261-6293c592-b206-499e-ae4d-05093d9c6d53.png)
![image](https://user-images.githubusercontent.com/40932902/168224307-c08a0b2d-b729-444e-a936-5fccc2999b77.png)
![image](https://user-images.githubusercontent.com/40932902/168224407-226b8d53-4a89-42e5-9ce5-4e4af45c807b.png)
![image](https://user-images.githubusercontent.com/40932902/168224541-0163716d-6b0b-4f0b-ae0d-9a37e64ac811.png)
![image](https://user-images.githubusercontent.com/40932902/168224573-460fe25b-19a8-4fdc-81aa-54cd4792688b.png)
![image](https://user-images.githubusercontent.com/40932902/168224663-03d74fb7-400a-4045-9452-b2152ecd0152.png)
