import pytest
import ochre
import numpy as np


def test_traing():
    letters = ["a", "b", "c", "x", "y", "z"]
    ts = {c: [ochre.get_letter(c)] for c in letters}
    ochre.training.train(ts)
