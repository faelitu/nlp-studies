# Installation:

# $ pip3 install -U gensim

# About:

# Gensim (https://pypi.python.org/pypi/gensim) is another important
# library. It is used primarily for topic modeling and document similarity.
# Gensim is most useful for tasks such as getting a word vector of a word.

import gensim
from gensim.models import Word2Vec
min_count = 0
size = 50
window = 2
sentences= "bitcoin is an innovative payment network and a new kind of money."
sentences=sentences.split()
print(sentences)

model = Word2Vec(sentences, min_count=min_count, size=size, window=window)
print(model)

print(model['a'])            # Vector for the character 'a'

# One can download the trained set of vectors from Google and figure
# out the representation for desired text, as follows:

# model = gensim.models.KeyedVectors.load_word2vec_
# format('GoogleNews-vectors-negative300.bin', binary=True)  
# sentence = ["I", "hope", "it", "is", "going", "good", "for", "you"]
# vectors = [model[w] for w in sentence]

# (You can use the following link to download the sample model:
# https://github.com/mmihaltz/word2vec-GoogleNews-vectors, or
# undertake a conventional search with the given name of the .bin file and
# paste it in your working directory.)
# Gensim offers LDA (latent dirichlet allocation—a generative statistical
# model that allows sets of observations to be explained by unobserved
# groups that explain why some parts of the data are similar) modules
# too. This allows both LDA model estimation from a training corpus and
# inference of topic distribution on new, unseen documents. The model can
# also be updated with new documents for online training.