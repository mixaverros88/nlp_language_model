from functions.read_dataset import get_reuters_files
from functions.helper_functions import normalize_corpus, generate_bigram, calculate_word_frequency, count_probabilities

corpus = get_reuters_files()
tokens = normalize_corpus(corpus)
bigram_list = generate_bigram(tokens)
word_frequency_dictionary = calculate_word_frequency(bigram_list)
word = 'review'.lower()
count_probabilities(word_frequency_dictionary, word, tokens)
