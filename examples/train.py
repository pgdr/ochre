#!/usr/bin/env python
import ochre
import ochre.training


def main(sentence, collection=True):
    print(sentence)
    box = lambda idx: (0, idx * 14, 14, (idx + 1) * 14)
    sentence_img = ochre.get_sentence(sentence)

    letters = sorted(set(sentence.replace(" ", "")))
    if collection:
        ts = {
            c: list(ochre.collection.collection(ochre.get_letter(c))) for c in letters
        }
    else:
        ts = {c: [ochre.get_letter(c)] for c in letters}
    nn = ochre.training.train(ts)

    prediction = [
        ochre.training.predict(nn, sentence_img, box=box(idx))
        for idx in range(len(sentence))
    ]
    print("".join(prediction))

    for idx, c in enumerate(sentence):
        if c == " ":
            print(f"Skipping space at idx={idx}")
            continue
        letter = ochre.training.predict(nn, sentence_img, box=box(idx))
        cor = "ok" if letter == c else "fail"
        print(f"{letter} == {c}     {cor}")


def _assert_letters(sentence):
    for c in sentence:
        if c == " ":
            continue
        assert ord("a") <= ord(c) <= ord("z"), f'"{c}" not in alphabet'


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: train hello world")

    collection = False  # noise, shear, up/down, etc
    if "--collection" in argv:
        collection = True
        argv.remove("--collection")
    sentence = " ".join(argv[1:]).lower()
    _assert_letters(sentence)
    main(sentence, collection=collection)
