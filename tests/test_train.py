import pytest
import ochre
import numpy as np


def test_traing():
    letters = ["a", "b", "c", "x", "y", "z"]
    ts = {c: [ochre.get_letter(c)] for c in letters}
    nn = ochre.training.train(ts)

    for letter in letters:
        c = ochre.get_letter(letter)
        res = nn.predict(c.reshape(1, -1))
        idx = res[0].argmax()
        assert (ord(letter) - ord("a")) == idx
