# There is a large number of things you could do to preprocess the text. For
# example, replacing one word with another, removing or adding some
# specific type of words, etc.

sentence = 'John has been selected for the trial phase this time. Congrats!!'
sentence=sentence.lower()
# defining the positive and negative words explicitly
positive_words=['awesome','good', 'nice', 'super', 'fun',
'delightful','congrats']
negative_words=['awful','lame','horrible','bad']
sentence=sentence.replace('!','')
print(sentence) # john has been selected for the trial phase this time. congrats

words= sentence.split(' ')
print(words) # ['john', 'has', 'been', 'selected', 'for', 'the', 'trial', 'phase', 'this', 'time.', 'congrats']

result = set(words) - set(positive_words)
print(result) # {'phase', 'time.', 'trial', 'this', 'for', 'has', 'selected', 'john', 'been', 'the'}