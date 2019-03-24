import freetype
import numpy as np

from . import generators
from . import training


def get_letter(c):
    return generators.char(c)


def get_word(word):
    letters = [generators.char(c) for c in word]
    img = letters[0]
    for i in range(1, len(letters)):
        img = np.concatenate((img, letters[i]), axis=1)
    return img


def get_sentence(sentence):
    words = [get_word(w) for w in sentence]
    img = words[0]
    for i in range(1, len(words)):
        img = np.concatenate((img, words[i]), axis=1)
    return img
