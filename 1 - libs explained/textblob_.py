# Installation:

# $ pip3 install -U textblob
# $ python3 -m textblob.download_corpora

# Applications:

# SENTIMENT ANALYSIS

# Polarity defines negativity or positivity in the sentence, whereas
# subjectivity implies whether the sentence discusses something vaguely or
# with complete surety.

from textblob import TextBlob
# Taking a statement as input
statement = TextBlob("My home is far away from my school.")
# Calculating the sentiment attached with the statement
print(statement.sentiment) # Sentiment(polarity=0.1, subjectivity=1.0)


# TAGGING

# Tagging is the process
# of denoting a word in a text (corpus) as corresponding to a particular part
# of speech.

# Defining a sample text
text = '''How about you and I go together on a walk far away
from this place, discussing the things we have never discussed
on Deep Learning and Natural Language Processing.'''
blob_ = TextBlob(text)           # Making it as Textblob object
print(blob_.tags) # [('How', 'WRB'), ('about', 'IN'), ('you', 'PRP'), ('and', 'CC'), ('I', 'PRP'), ('go', 'VBP'), 
                  # ('together', 'RB'), ('on', 'IN'), ('a', 'DT'), ('walk', 'NN'), ('far', 'RB'), ('away', 'RB'), 
                  # ('from', 'IN'), ('this', 'DT'), ('place', 'NN'), ('discussing', 'VBG'), ('the', 'DT'), 
                  # ('things', 'NNS'), ('we', 'PRP'), ('have', 'VBP'), ('never', 'RB'), ('discussed', 'VBN'), 
                  # ('on', 'IN'), ('Deep', 'NNP'), ('Learning', 'NNP'), ('and', 'CC'), ('Natural', 'NNP'), 
                  # ('Language', 'NNP'), ('Processing', 'NNP')]


# DEALING WITH SPELLING ERRORS

sample_ = TextBlob("I thinkk the model needs to be trained more!")
print(sample_.correct()) # I think the model needs to be trained more!


# LANGUAGE TRANSLATION

lang_ = TextBlob("Voulez-vous apprendre le français?")
english = lang_.translate(from_lang='fr', to='en')
print(english) # Do you want to learn French?
portugues = english.translate(from_lang='en', to='pt')
print(portugues) # Você quer aprender francês?
print(lang_.translate(from_lang='fr', to='pt-br')) # Você quer aprender francês?

ex = "Please, everyone stay in line!"
ex_blob = TextBlob(ex)
ex_pt = ex_blob.translate(from_lang='en', to='pt')
ex_pt_br = ex_blob.translate(from_lang='en', to='pt-br')
print(ex_pt) # Por favor, todos fiquem na fila!
print(ex_pt_br) # Por favor, todos fiquem na fila!
# Pelo visto, o 'pt' é brasileiro mesmo