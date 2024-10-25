import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)

    def stem(self, word):
        return self.stemmer.stem(word.lower())

    def preprocess(self, sentence):
        tokens = self.tokenize(sentence)
        tokens = [self.stem(word) for word in tokens if word.lower() not in self.stop_words]
        return tokens

    def bag_of_words(self, tokenized_sentence, words):
        sentence_words = [self.stem(word) for word in tokenized_sentence]
        bag = np.zeros(len(words), dtype=np.float32)
        for idx, w in enumerate(words):
            if w in sentence_words:
                bag[idx] = 1
        return bag