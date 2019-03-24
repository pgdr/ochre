#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import ochre


def main(sent):
    shi = 7
    img = ochre.get_sentence(sent)
    for i in range(shi * 2):
        img_ = ochre.generators.shift(ochre.get_sentence(sent), i - shi, 0)
        img = np.concatenate((img, img_), axis=1)
    for i in range(shi * 2):
        img_ = ochre.generators.shift(ochre.get_sentence(sent), 0, i - shi)
        img = np.concatenate((img, img_), axis=1)

    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: manipulates.py hello world")
    main(" ".join(argv[1:]))
