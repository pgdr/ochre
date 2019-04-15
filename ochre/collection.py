import numpy as np
import ochre


def _generate(img, op):
    i = 0
    while True:
        i += 1
        yield op(img, i)


def noise(img):
    while True:
        img = np.random.normal(2*img + 2, 20)
        yield img


def up(img):
    f = lambda img, i: ochre.generators.shift(img, i, 0)
    for e in _generate(img, f):
        yield e


def down(img):
    f = lambda img, i: ochre.generators.shift(img, -i, 0)
    for e in _generate(img, f):
        yield e


def left(img):
    f = lambda img, i: ochre.generators.shift(img, 0, i)
    for e in _generate(img, f):
        yield e


def right(img):
    f = lambda img, i: ochre.generators.shift(img, 0, -i)
    for e in _generate(img, f):
        yield e


def slash(img):
    f = lambda img, i: ochre.generators.shear(img, shearing=i)
    for e in _generate(img, f):
        yield e


def backslash(img):
    f = lambda img, i: ochre.generators.shear(img, shearing=-i)
    for e in _generate(img, f):
        yield e


def collection(img, num=2):
    yield img

    for op in (up, down, left, right, slash, backslash, noise):
        img_gen = op(img)
        for idx, img_ in enumerate(img_gen):
            yield img_
            if idx >= num:
                break
