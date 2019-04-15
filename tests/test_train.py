import ochre
import ochre.training
import numpy as np


def _get_nn(letters, n_copies=1, collection=False):
    if not collection:
        ts = {c: [ochre.get_letter(c) for _ in range(n_copies)] for c in letters}
    else:
        for c in letters:
            ts = {
                c: list(ochre.collection.collection(ochre.get_letter(c)))
                for c in letters
            }
    nn = ochre.training.train(ts)
    return nn


def test_training():
    letters = ["a", "b", "c", "x", "y", "z"]
    nn = _get_nn(letters)

    for letter in letters:
        c = ochre.get_letter(letter)
        assert ochre.training.predict(nn, c) == letter


def test_collection_training():
    letters = "abcdefghijklxyz"
    nn = _get_nn(letters, n_copies=1, collection=True)

    for letter in letters:
        c = ochre.get_letter(letter)
        vec = ochre.training.predict_vector(nn, c)
        assert ochre.training.predict(nn, c) == letter, vec


def test_mulitple_training():
    letters = ["a", "b", "c", "x", "y", "z"]
    nn = _get_nn(letters, n_copies=1)

    for letter in letters:
        c = ochre.get_letter(letter)
        vec = ochre.training.predict_vector(nn, c)
        assert ochre.training.predict(nn, c) == letter, vec


def test_sentence():
    box = lambda idx: (0, idx * 14, 14, (idx + 1) * 14)
    sentence = "my first word".lower()
    sentence_img = ochre.get_sentence(sentence)

    letters = sorted(set(sentence.replace(" ", "")))
    nn = _get_nn(letters)

    for idx, c in enumerate(sentence):
        if c == " ":
            print(f"Skipping space at idx={idx}")
            continue
        letter = ochre.training.predict(nn, sentence_img, box=box(idx))
        assert letter == c
