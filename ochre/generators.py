import os
import freetype
import numpy as np


def _get_face(width: int = 14, height: int = 14, serif: bool = False):
    facename = os.path.join("data", "DejaVuSerif.ttf" if serif else "DejaVuSans.ttf")
    face = freetype.Face(facename)
    face.set_pixel_sizes(width, height)
    return face


def _np_pad_to(ndarr: np.ndarray, width: int, height: int):
    shape = ndarr.shape
    assert shape[0] <= height, f"{shape[0]} !<= height = {height}"
    assert shape[1] <= width, f"{shape[1]} !<= width = {width}"
    top = (height - shape[0]) // 2
    bot = int((height - shape[0]) / 2 + 0.5)
    left = (width - shape[1]) // 2
    right = int((width - shape[1]) / 2 + 0.5)
    return np.pad(ndarr, [(top, bot), (left, right)], mode="constant")


def char(c: chr, width: int = 14, height: int = 14, serif: bool = False):
    face = _get_face(width=width, height=height, serif=serif)
    face.load_char(c)
    bitmap = face.glyph.bitmap
    arr = np.array(bitmap.buffer).reshape((bitmap.rows, bitmap.width))
    return _np_pad_to(arr, height, width)


def shift(img: np.ndarray, top: int, left: int):
    """Shift the image `top` pixels from the top (can be negative) and
       `left` pixels from the left.  Does not rotate.
    """
    abs_top = abs(top)
    abs_left = abs(left)
    shape = img.shape
    img = _np_pad_to(img, width=shape[1] + 2 * abs_left, height=shape[0] + 2 * abs_top)
    vert = (2 * abs_top, shape[0] + 2 * abs_top) if top < 0 else (0, shape[0])
    hori = (2 * abs_left, shape[1] + 2 * abs_left) if left < 0 else (0, shape[1])
    shape_ = img.shape
    return img[vert[0] : vert[1], hori[0] : hori[1]]


def shear(img, shearing=10):
    top, left = img.shape
    img_ = np.zeros((top, left + abs(shearing)), dtype=img.dtype)
    for y in range(top):
        current = top - y if shearing >= 0 else y
        pad = (abs(shearing) * current) // top
        img_[y, pad : pad + left] = img[y, :]
    res = img_[0:top, 0:left]
    assert res.shape == img.shape, f"{res.shape} != {img.shape}"
    return res
