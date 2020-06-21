import re
import numpy as np
from nltk.corpus import wordnet as wn

# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('punkt')

from model_init import load_model
print('loading model')
model = load_model()
print('model loaded')

sent1 = "The current from the wire hurt"
word1 = "current"


def get_words(in_word):
    syns = wn.synsets(in_word)
    ret = []
    for syn in syns:
        ret_list = []
        for lem in syn.lemmas():
            lemma_name = lem.name()
            lemma_name = lemma_name.replace('_', ' ')
            if lemma_name != in_word:
                ret_list.append(lemma_name)
        if len(ret_list) > 0:
            ret.append(ret_list)
    return ret


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def get_best_words(word, sent):
    syn = get_words(word)
    parts = re.split(f'{word}', sent)
    oldSent = model.encode([sent])[0]
    oldWord = word

    synMax = -float('inf')
    bestWords = []
    wordMax = -float('inf')
    bestWord = ''

    for synset in syn:
        total = 0
        for w in synset:
            newSent = f'{w}'.join(parts)
            sim = cosine(model.encode([newSent])[0], oldSent)
            if sim > wordMax:
                bestWord = w
                wordMax = sim
            total += sim
            print(f'{w} and {sim}')
        avg = total / len(synset)
        print(f'{synset} and {avg}')
        if avg > synMax:
            bestWords = synset
            synMax = avg

    print(bestWords)

    print(f'best word indiv: {bestWord}')


get_best_words(word1, sent1)
