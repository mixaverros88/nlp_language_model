from functions.read_dataset import get_test_file
from functions.helper_functions import normalize_corpus, generate_bigram, calculate_word_frequency, count_probabilities

print('\n\n Test With sample-text.txt \n\n')

corpus = get_test_file('test2')
tokens = normalize_corpus(corpus)
bigram_list = generate_bigram(tokens)
word_frequency_dictionary = calculate_word_frequency(bigram_list)
word = 'mln'.lower()
print(count_probabilities(word_frequency_dictionary, word, tokens))
# assert sum_of_paragraphs(text) == 8, 'Should be 8'
