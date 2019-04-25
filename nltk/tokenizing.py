from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import sent_tokenize as st
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer as rt


text = "Hi Mr. Smith! I'm going to buy some vegetables (tomatoes and cucumbers). From the store, you know?"

#print(wt(text))

#print(st(text))

'''
# ngrams
words = wt(text)
print(list(ngrams(words,4)))
'''

# regexp tokenizer
#cap_tokenizer = rt("[A-Z]\w+") # it's a specification of regexp tokenizer
#print(cap_tokenizer.tokenize(text))


