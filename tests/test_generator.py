import numpy as np
import ochre


def test_shift():
    img = ochre.get_word("help")
    shape = img.shape
    assert np.count_nonzero(img[0:4, 0 : shape[1]]) != 0  # for sanitary purposes only

    img = ochre.generators.shift(img, 4, 7)
    assert np.count_nonzero(img[0:4, 0 : shape[1]]) == 0
    assert np.count_nonzero(img[0 : shape[0], 0:7]) == 0


def test_collection():
    img = ochre.get_word("help")
    shape = img.shape
    assert np.count_nonzero(img[0:4, 0 : shape[1]]) != 0  # for sanitary purposes only

    imgs = list(ochre.collection.collection(img))
