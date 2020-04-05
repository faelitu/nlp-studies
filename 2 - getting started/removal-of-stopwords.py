# A stopword is a commonly used word (such as the) that a search engine
# has been programmed to ignore.

import nltk
from nltk import word_tokenize
sentence= "This book is about Deep Learning and Natural Language Processing!"
tokens = word_tokenize(sentence)
print(tokens) # ['This', 'book', 'is', 'about', 'Deep', 'Learning', 'and', 'Natural', 'Language', 'Processing', '!']

# nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
new_tokens = [w for w in tokens if not w in stop_words]
print(new_tokens) # ['This', 'book', 'Deep', 'Learning', 'Natural', 'Language', 'Processing', '!']