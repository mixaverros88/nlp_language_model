from nltk.tokenize import word_tokenize
from nltk.util import bigrams
import re


def normalize_corpus(corpus):
    corpus = corpus.lower()
    corpus = text_cleaner(corpus)
    tokens = word_tokenize(corpus)
    return tokens


def generate_bigram(tokens):
    return list(bigrams(tokens))


def calculate_word_frequency(bigram_list):
    word_frequency_dictionary = {}
    for i in bigram_list:
        if not word_frequency_dictionary.__contains__(i):
            dictionary = {i: 1}
        else:
            count = word_frequency_dictionary.pop(i)  # get the value
            dictionary = {i: count + 1}
        word_frequency_dictionary.update(dictionary)
    return word_frequency_dictionary


# p(w1...ws) = p(w1) . p(w2 | w1) . p(w3 | w1 w2) . p(w4 | w1 w2 w3) ..... p(wn | w1...wn-1)
# p(w1...ws) = p(w1) . p(w2 | w1)
def conditional_probability(words, bigram_list, tokens_list):
    tokens = word_tokenize(words)
    prob = 0
    total_prob = 0
    word_frequency_dictionary = calculate_word_frequency(bigram_list)
    for i, value in enumerate(tokens):
        if i == 0:
            count = tokens_list.count(value)
            prob = count / len(tokens_list)
        if i > 0:
            dict = count_probabilities(word_frequency_dictionary, value, tokens)
            pp = dict.get(tokens[0] + ' ' + tokens[1])
            print(pp)
            total_prob = prob * pp
    return total_prob


def count_probabilities(word_frequency_dictionary, given_word, tokens):
    dict = {}
    for key, value in word_frequency_dictionary.items():
        if key[0] == given_word:
            count = value / tokens.count(given_word)
            dict[given_word + ' ' + key[1]] = float(count)
    return dict


def text_cleaner(text):
    # lower case text
    new_string = text.lower()
    new_string = re.sub(r"'s\b", "", new_string)
    # remove punctuations
    new_string = re.sub("[^a-zA-Z]", " ", new_string)
    long_words = []
    # remove short word
    for i in new_string.split():
        if len(i) >= 3:
            long_words.append(i)
    return (" ".join(long_words)).strip()


def tokenize_raw_text(raw_text_path: str, token_text_path: str) -> None:
    """
    Read a input text file and write its content to an output text file in the form of tokenized sentences
    :param raw_text_path: path of raw input text file
    :param token_text_path: path of tokenized output text file
    """

    with open(raw_text_path) as read_handle, open(token_text_path, 'w') as write_handle:
        for paragraph in read_handle:
            paragraph = paragraph.lower()
    paragraph = replace_characters(paragraph)

    for tokenized_sentence in generate_tokenized_sentences(paragraph):
        write_handle.write(','.join(tokenized_sentence))
    write_handle.write('\n')
