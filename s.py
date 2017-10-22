# coding: utf-8

from gensim.models import word2vec
import sys

MODEL_PATH = './names.bin'

if __name__ == "__main__":
    model = word2vec.Word2Vec.load_word2vec_format(MODEL_PATH, binary=True)
    name = sys.argv[1]
    topn = 5
    if len(sys.argv) == 3:
        topn = int(sys.argv[2])
    try:
        results = model.most_similar(name.replace(' ', '_'), topn=topn)
    except:
        print('')
        sys.exit()
    for result in results:
        print('{0:.5f} {1}'.format(result[1], result[0].replace('_', ' ')))
    print('')
