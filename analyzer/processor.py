import nltk
import string
import operator
from nltk.corpus import stopwords
from collections import Counter


LANGUAGE = 'english'


def auto_reply(question):
    tokens = cleanup(question)
    if tokens:
        return sorted(
                Counter(tokens).items(),
                key=operator.itemgetter(1),
                reverse=True
        )

  
def cleanup(sentence):
    s = sentence.strip().replace('..', '').replace('...', '')  # to get rid of '..' and '...'
    tmp = [ token for token in nltk.word_tokenize(s) if token not in string.punctuation ]
    tokens = []
    for token in tmp: #TODO: figure out 'nested list comprehension', and make this bit more pythonic
        if token.lower() not in stopwords.words(LANGUAGE):
            tokens.append(token.title())
    return tokens
