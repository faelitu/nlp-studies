# Regular expressions are a very useful means of searching for a particular
# type of design or wordset from a given text. A regular expression (RE)
# specifies a set of strings that match it. The functions in this module allow
# you to check if a given string matches a particular RE (or if a given RE
# matches a particular string, which comes down to the same thing).

# Text search across the sentence using Regular expression
import re
words = ['very','nice','lecture','day','moon']
expression = '|'.join(words)
result = re.findall(expression, 'i attended a very nice lecture lastyear', re.M)
print(result) # ['very', 'nice', 'lecture']