# Installation:

# $ pip3 install spacy
# $ python3 -m spacy download en_core_web_sm

# You can now load the model via spacy.load('en_core_web_sm')

# About:

# SpaCy (https://spacy.io/) provides very fast and accurate syntactic
# analysis (the fastest of any library released) and also offers named entity
# recognition and ready access to word vectors. It is written in Cython
# language and contains a wide variety of trained models on language
# vocabularies, syntaxes, word-to-vector transformations, and entities
# recognition.

# Note: Entity recognition is the process used to classify multiple
# entities found in a text in predefined categories, such as a person,
# objects, location, organizations, dates, events, etc. Word vector refers
# to the mapping of the words or phrases from vocabulary to a vector
# of real numbers.

# Applications:

# ENTITY RECOGNITION

import spacy
# Run below command, if you are getting error
# python -m spacy download en
nlp = spacy.load("en")

william_wikidef = """William was the son of King William
II and Anna Pavlovna of Russia. On the abdication of his
grandfather  William I in 1840, he became the Prince of Orange.
On the death of his father in 1849, he succeeded as king of the
Netherlands. William married his cousin Sophie of Württemberg
in 1839 and they had three sons, William, Maurice, and
Alexander, all of whom predeceased him. """

nlp_william = nlp(william_wikidef)

print([ (i, i.label_, i.label) for i in nlp_william.ents])

# DEPENDENCY PARSING

# SpaCy also offers dependency parsing, which could be further utilized
# to extract noun phrases from the text, as follows:

# Noun Phrase extraction
senten_ = nlp('The book deals with NLP')
for noun_ in senten_.noun_chunks:
    print(noun_)
    print(noun_.text)
    print('---')
    print(noun_.root.dep_)
    print('---')
    print(noun_.root.head.text)