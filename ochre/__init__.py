import freetype
import numpy as np

from . import generators
from . import training
from . import collection


def get_letter(c, serif=False):
    return generators.char(c, serif=serif)


def get_word(word, serif=False):
    letters = [generators.char(c, serif=serif) for c in word]
    img = letters[0]
    for i in range(1, len(letters)):
        img = np.concatenate((img, letters[i]), axis=1)
    return img


def get_sentence(sentence, serif=False):
    words = [get_word(w, serif=serif) for w in sentence]
    img = words[0]
    for i in range(1, len(words)):
        img = np.concatenate((img, words[i]), axis=1)
    return img
