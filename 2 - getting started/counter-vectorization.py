# Counter vectorization is a SciKit-Learn library tool that takes any mass of
# text and returns each unique word as a feature, with a count of the number
# of times a particular word occurs in the text.

from sklearn.feature_extraction.text import CountVectorizer
texts=["Ramiess sings classic songs","he listens to old pop ",
       "and rock music", ' and also listens to classical songs']
cv = CountVectorizer()
cv_fit=cv.fit_transform(texts)
print(cv.get_feature_names()) # ['also', 'and', 'classic', 'classical', 'he', 'listens',
                              #  'music', 'old', 'pop', 'ramiess', 'rock', 'sings',
                              #  'songs', 'to']

print(cv_fit.toarray()) # [[0 0 1 0 0 0 0 0 0 1 0 1 1 0]  -> qtd de cada palavra na primeira frase
                        #  [0 0 0 0 1 1 0 1 1 0 0 0 0 1]  -> qtd de cada palavra na segunda frase
                        #  [0 1 0 0 0 0 1 0 0 0 1 0 0 0]  -> qtd de cada palavra na terceira frase
                        #  [1 1 0 1 0 1 0 0 0 0 0 0 1 1]] -> qtd de cada palavra na quarta frase
