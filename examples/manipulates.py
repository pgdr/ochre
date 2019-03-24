#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import ochre


def show_shift(sent):
    shi = 2  # number of shifts each direction
    img = ochre.get_sentence(sent)
    for i in range(shi * 2):
        img_ = ochre.generators.shift(ochre.get_sentence(sent), 2 * (i - shi), 0)
        img = np.concatenate((img, img_), axis=1)
    for i in range(shi * 2):
        img_ = ochre.generators.shift(ochre.get_sentence(sent), 0, 2 * (i - shi))
        img = np.concatenate((img, img_), axis=1)

    plt.imshow(img)
    plt.show()


def show_shear(sent):
    she = 7
    img = ochre.get_sentence(sent)

    img_ = ochre.generators.shear(ochre.get_sentence(sent), shearing=she)
    img = np.concatenate((img, img_), axis=1)

    img_ = ochre.generators.shear(ochre.get_sentence(sent), shearing=-she)
    img = np.concatenate((img, img_), axis=1)

    plt.imshow(img)
    plt.show()


def main(sent):
    show_shear(sent)
    show_shift(sent)


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: manipulates.py hello world")
    main(" ".join(argv[1:]))
