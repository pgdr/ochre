import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC


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


def _non_neural(c):
    return ord(c) - ord("a")


def train(training_set: dict, width: int = 14, height: int = 14):
    """The input dict must be a set mapping letters to a list of ndarrays"""
    _assert_training_set(training_set, width, height)

    _neural = False
    if _neural:
        classifier = _get_network(width, height)
    else:
        classifier = SVC(gamma=0.001)
    X = []
    for x in training_set:
        for img in training_set[x]:
            print(len(X))
            X.append(img.reshape(1, -1))

    X = np.array(X)
    X = X.reshape((len(X), (width * height)))
    print(X.shape)

    if _neural:
        y = np.array([_letter_vector(x) for _ in training_set[x] for x in training_set])
    else:
        _y = []
        for x, lst in training_set.items():
            _y.extend([_non_neural(x) for _ in lst])
        y = np.array(_y)
    print(y.shape)
    print(y)
    classifier.fit(X, np.array(y))
    return classifier


def predict_vector(nn, img, box=None):
    if box is not None:
        img = img[box[0] : box[2], box[1] : box[3]]
    img = img.reshape(1, -1)
    outlayer = nn.predict(img)
    return outlayer[0]


def predict(nn, img, box=None):
    vec = predict_vector(nn=nn, img=img, box=box)
    idx = vec.argmax()
    _neural = False
    if _neural:
        if vec[idx] < 0.8 or len([e for e in vec if e > 0.5]) > 2:
            return " "
        return chr(idx + ord("a"))

    return chr(ord("a") + int(vec))
