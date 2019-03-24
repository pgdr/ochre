#!/usr/bin/env python
import os
import matplotlib.pyplot as plt
import numpy as np
import ochre


def show_collection(char):
    ori = ochre.get_letter(char)
    img = ochre.get_letter(char)
    for img_ in ochre.collection.collection(ori):
        img = np.concatenate((img, img_), axis=1)
    plt.imshow(img)
    plt.show()


def train_collection(chars):
    ts = {
        c: list(ochre.collection.collection(ochre.get_letter(c), num=1)) for c in chars
    }
    nn = ochre.training.train(ts)


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: collection.py char")
    if len(argv) == 2:
        print(f"Showing letter {argv[1]}")
        show_collection(argv[1])
    else:
        print("Training on collection")
        train_collection(argv[1:])
