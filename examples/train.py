#!/usr/bin/env python
import ochre.training


def main(letters):
    print(letters)
    ts = {c: [ochre.get_letter(c)] for c in letters}
    nn = ochre.training.train(ts)

    for letter in letters:
        c = ochre.get_letter(letter)
        pred = ochre.training.predict(nn, c)
        cor = "ok" if letter == pred else "fail"
        print(f"{letter} == {pred}     {cor}")


def _assert_letters(args):
    for c in args:
        assert len(c) == 1, f'"{c}" in args not a letter'
        assert ord("a") <= ord(c) <= ord("z"), f'"{c}" not in alphabet'


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: train a b c ...")
    args = argv[1:]
    _assert_letters(args)
    main(args)
