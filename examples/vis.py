#!/usr/bin/env python

import ochre
import matplotlib.pyplot as plt


def vis_char(char):
    img = ochre.get_letter(char)
    return img


def vis_word(word):
    img = ochre.get_word(word)
    return img


def vis_sentence(sent):
    img = ochre.get_sentence(sent)
    return img


def main(args):
    if len(args) == 1:
        img = vis_char(arg) if len(arg) == 1 else vis_word(arg)
    else:
        img = vis_sentence(" ".join(args))
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: vis.py chars/words")
    main(argv[1:])
