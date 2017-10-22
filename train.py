# coding: utf-8

import logging
from gensim.models import word2vec

SENTENCES_PATH = './names.txt'
MODEL_PATH = './names.bin'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence(SENTENCES_PATH)
model = word2vec.Word2Vec(
    sentences,
    size=150,
    window=7,
    min_count=10,
    workers=4
)
model.save_word2vec_format(MODEL_PATH, binary=True)
