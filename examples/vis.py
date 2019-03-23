#!/usr/bin/env python

import ochre
import matplotlib.pyplot as plt


def main(char):
    letter = ochre.get_letter(char)
    plt.imshow(letter)
    plt.show()


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        exit("Usage: vis.py char")
    main(argv[1])
