#!/usr/bin/env python
import ochre

def main(letters):
    print(letters)
    ts = {c: [ochre.get_letter(c)] for c in letters}
    nn = ochre.training.train(ts)

    for letter in letters:
        print()
        print('=' * 10 + letter.center(5) + '='*10)
        c = ochre.get_letter(letter)
        res = nn.predict(c.reshape(1, -1))
        print(letter)
        print(res)
        print(res[0].argmax())
        print('=' * 25)
        print()

if __name__ == '__main__':
    from sys import argv

    if len(argv) < 2:
        exit('Usage: train a b c ...')
    main(argv[1:])
