# TF-IDF is an acronym of two terms: term frequency and inverse document
# frequency. TF is the ratio representing the count of specific words to the
# total number of words in a document. Suppose that a document contains
# 100 words, wherein the word happy appears five times. The term frequency
# (i.e., tf) for happy is then (5/100) = 0.05. IDF, on the other hand, is a
# log ratio of the total number of documents to a document containing a
# particular word. Suppose we have 10 million documents, and the word
# happy appears in 1,000 of them. The inverse document frequency (i.e., idf),
# then, would be calculated as log (10,000,000/1,000) = 4. Thus, the TF-­IDF
# weight is the product of these quantities: 0.05 × 4 = 0.20.

# Note: Along similar lines as TF-IDF is BM25, which is used to score
# a document on the basis of its relation to a query. BM25 ranks a
# set of documents using the query terms of each of the documents,
# irrespective of the relationship between the keywords of the query
# within a document.

from sklearn.feature_extraction.text import TfidfVectorizer
texts=["Ramiess sings classic songs","he listens to old pop",
       "and rock music", ' and also listens to classical songs']
vect = TfidfVectorizer()
X = vect.fit_transform(texts)
print(X.todense()) # [[0.         0.         0.52547275 0.         0.         0.         
                   #   0.         0.         0.         0.52547275 0.         0.52547275
                   #   0.41428875 0.        ]
                   #  [0.         0.         0.         0.         0.48546061 0.38274272
                   #   0.         0.48546061 0.48546061 0.         0.         0.
                   #   0.         0.38274272]
                   #  [0.         0.48693426 0.         0.         0.         0.
                   #   0.61761437 0.         0.         0.         0.61761437 0.
                   #   0.         0.        ]
                   #  [0.47212003 0.37222485 0.         0.47212003 0.         0.37222485
                   #   0.         0.         0.         0.         0.         0.
                   #   0.37222485 0.37222485]]