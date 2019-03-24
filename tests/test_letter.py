import ochre
import numpy as np


def test_letter():
    x = ochre.get_letter("x")
    assert isinstance(x, np.ndarray)
