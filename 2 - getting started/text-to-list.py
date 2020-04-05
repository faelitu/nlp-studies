# You can read a text file and convert it into a list of words or list of sentences,
# according to your needs.

text_file = 'data.txt'
# Method-1 : Individual words as separate elements of the list
with open(text_file) as f:
    words = f.read().split()
print(words) # ['Are', 'you', 'sure', 'moving', 'ahead', 'on', 'this', 'route', 'is', 'the', 'right', 'thing?']

# Method-2 : Whole text as single element of the list
f = open(text_file , 'r')
words_ = f.readlines()
print(words_) # ['Are you sure moving ahead on this route is the right thing?\n']