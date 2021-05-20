from nltk.tokenize import word_tokenize
from nltk.util import bigrams
import re


def normalize_corpus(corpus):
    # TODO: remove punctiation
    corpus = corpus.lower()
    corpus = text_cleaner(corpus)
    tokens = word_tokenize(corpus)
    return tokens


def generate_bigram(tokens):
    return list(bigrams(tokens))


def calculate_word_frequency(bg):
    word_frequency_dictionary = {}
    for i in bg:
        if not word_frequency_dictionary.__contains__(i):
            dictionary = {i: 1}
        else:
            count = word_frequency_dictionary.pop(i)  # get the value
            dictionary = {i: count + 1}
        word_frequency_dictionary.update(dictionary)
    return word_frequency_dictionary


def count_probabilities(word_frequency_dictionary, word, tokens):
    #listTo = ['', '']
    for key, value in word_frequency_dictionary.items():
        if key[0] == word:
            count = value / tokens.count(word)
            #listTo.append(word + ' ' + key[1], str(count))
            print(word + ' ' + key[1] + ' : ' + str(count))
    #return listTo


def text_cleaner(text):
    # lower case text
    newString = text.lower()
    newString = re.sub(r"'s\b", "", newString)
    # remove punctuations
    newString = re.sub("[^a-zA-Z]", " ", newString)
    long_words = []
    # remove short word
    for i in newString.split():
        if len(i) >= 3:
            long_words.append(i)
    return (" ".join(long_words)).strip()
