from functions.read_dataset import get_reuters_files
from functions.helper_functions import normalize_corpus
from models.UniformLanguageModel import UniformLanguageModel
from models.UnigramLanguageModel import UnigramLanguageModel
from models.LaplaceBigramLanguageModel import LaplaceBigramLanguageModel
from models.StupidBackoffLanguageModel import StupidBackoffLanguageModel
from models.CustomLanguageModel import CustomLanguageModel
from models.LaplaceUnigramLanguageModel import LaplaceUnigramLanguageModel
from models.Sentence_Corrector import Sentence_Corrector
from nltk.tokenize import sent_tokenize

corpus = get_reuters_files()
# corpus = normalize_corpus(corpus)
# print(corpus)
corpus = sent_tokenize(corpus)
# print(corpus)
given_word = 'the'

uniformLangModel = UniformLanguageModel(corpus)
uniformLangModel.train(corpus)
uniform_score = uniformLangModel.score(given_word)
print('UniformLanguageModel: ', uniform_score)

unigramLanguageModel = UnigramLanguageModel(corpus)
unigramLanguageModel.train(corpus)
unigram_score = unigramLanguageModel.score(given_word)
print('UnigramLanguageModel:', unigram_score)

laplaceBigram = LaplaceBigramLanguageModel(corpus)
laplaceBigram.train(corpus)
laplaceBigram_score = laplaceBigram.score(given_word)
print('LaplaceBigramLanguageModel:', laplaceBigram_score)

laplaceUnigramLanguageModel = LaplaceUnigramLanguageModel(corpus)
laplaceUnigramLanguageModel.train(corpus)
laplaceUnigramLanguageModel_score = laplaceUnigramLanguageModel.score(given_word)
print('LaplaceUnigramLanguageModel:', laplaceUnigramLanguageModel_score)

stupidBackoffLanguageModel = StupidBackoffLanguageModel(corpus)
stupidBackoffLanguageModel.train(corpus)
stupidBackoffLanguageModel_score = stupidBackoffLanguageModel.score(given_word)
print('StupidBackoffLanguageModel:', stupidBackoffLanguageModel_score)

customLanguageModel = CustomLanguageModel(corpus)
customLanguageModel.train(corpus)
customLanguageModel_score = customLanguageModel.score(given_word)
print('CustomLanguageModel:', customLanguageModel_score)

spellCorrect = Sentence_Corrector()
spellCorrect_result = spellCorrect.return_best_sentence('my name are mike')
print(spellCorrect_result)

spellCorrect_result = spellCorrect.return_best_sentence('this is wrong spalled word')
print(spellCorrect_result)
# bigram_list = generate_bigram(tokens)
# conditional_probability('name george', bigram_list, tokens)
# word_frequency_dictionary = calculate_word_frequency(bigram_list)
# given_word = 'review'.lower()
# print(count_probabilities(word_frequency_dictionary, given_word, tokens))
