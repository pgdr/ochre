#!/usr/bin/env python
import os
import matplotlib.pyplot as plt
import ochre


def plot_figures(figures):
    width = int((len(figures)) ** 0.5)
    height = (len(figures) // width) + 1

    f, axarr = plt.subplots(width, height)
    for i, fig in enumerate(figures):
        x = i % width
        y = i // width
        axarr[x, y].imshow(fig)
    return f, axarr


def vis_sentence(sent):
    coll = list(
        ochre.collection.collection(ochre.get_sentence(sent, serif=os.getenv("SERIF")))
    )
    return coll


def main(args):
    coll = vis_sentence(" ".join(args))
    plot_figures(coll)
    plt.show()


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: vis.py chars/words")
    main(argv[1:])
