import numpy as np
from sklearn.neural_network import MLPClassifier


def _get_network(width: int, height: int):
    layers = (width * height, width * height * 3, 26)
    return MLPClassifier(
        solver="lbfgs", alpha=1e-5, hidden_layer_sizes=layers, random_state=1
    )


def _assert_training_set(ts: dict, width: int, height: int):
    assert ts
    for x in ts:
        assert isinstance(x, str) and len(x) == 1, f'"{x}" not a letter'
        assert ord("a") <= ord(x) <= ord("z"), f'"{x}" not in range'
        assert isinstance(ts[x], list), f'ts[x] = "{ts[x]}" not a list'
        for img in ts[x]:
            assert isinstance(img, np.ndarray), f"not an ndarray: {ts[x]}"
            assert img.shape == (
                width,
                height,
            ), f"Shape {img.shape} != {(width, height)}"


def _letter_vector(c):
    vec = [0 for _ in range(26)]
    vec[ord(c) - ord("a")] = 1
    return vec


def train(training_set: dict, width: int = 14, height: int = 14):
    """The input dict must be a set mapping letters to a list of ndarrays"""
    _assert_training_set(training_set, width, height)
    nn = _get_network(width, height)
    X = []
    for x in training_set:
        for img in training_set[x]:
            print(len(X))
            X.append(img.reshape(1, -1))
    X = np.array(X)
    X = X.reshape((len(training_set.items()), width * height))
    print(X.shape)
    y = np.array([_letter_vector(x) for _ in training_set[x] for x in training_set])
    print(y.shape)
    nn.fit(X, np.array(y))
    return nn


def predict(nn, img, box=None):
    if box is not None:
        img = img[box[0] : box[2], box[1] : box[3]]
    img = img.reshape(1, -1)
    res = nn.predict(img)
    idx = res[0].argmax()
    if res[0][idx] < 0.8 or len([e for e in res[0] if e > 0.5]) > 2:
        return " "
    return chr(idx + ord("a"))
