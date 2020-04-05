# Installation:

# $ pip3 install Pattern

# About:

# Pattern (https://pypi.python.org/pypi/Pattern) is useful for a variety
# of NLP tasks, such as part-of-speech taggers, n-gram searches, sentiment
# analysis, and WordNet and machine learning, such as vector space
# modeling, k-means clustering, Naive Bayes, K-NN, and SVM classifiers.

import pattern3
from pattern3.en import tag
tweet_ = "I hope it is going good for you!"
tweet_l = tweet_.lower()
tweet_tags = tag(tweet_l)
print(tweet_tags)