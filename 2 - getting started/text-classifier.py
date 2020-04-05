# Text can be classified into various classes, such as positive and negative.
# TextBlob offers many such architectures.

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
data = [
('I love my country.', 'pos'),
('This is an amazing place!', 'pos'),
('I do not like the smell of this place.', 'neg'),
('I do not like this restaurant', 'neg'),
('I am tired of hearing your nonsense.', 'neg'),
("I always aspire to be like him", 'pos'),
("It's a horrible performance.", "neg")
]
model = NaiveBayesClassifier(data)
result = model.classify("It's an awesome place!")

print(result) # pos