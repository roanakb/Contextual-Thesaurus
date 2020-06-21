import re
import numpy as np
from nltk.corpus import wordnet as wn

# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('punkt')

from model_init import model


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


def get_best_words(word, sent, syn):
    parts = re.split(f'{word}', sent)
    old_sent = model.encode([sent])[0]

    syn_max = -float('inf')
    best_words = []
    word_max = -float('inf')
    best_word = ''

    for synset in syn:
        total = 0
        for w in synset:
            new_sent = f'{w}'.join(parts)
            sim = cosine(model.encode([new_sent])[0], old_sent)
            if sim > word_max:
                best_word = w
                word_max = sim
            total += sim
            print(f'{w} and {sim}')
        avg = total / len(synset)
        print(f'{synset} and {avg}')
        if avg > syn_max:
            best_words = synset
            syn_max = avg
    print(best_words)

    print(f'best word indiv: {best_word}')

    return best_words
