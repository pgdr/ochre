import os
import freetype
import numpy as np


def _get_face(width: int = 14, height: int = 14, serif: bool = False):
    facename = os.path.join("data", "DejaVu.ttf" if serif else "DejaVuSans.ttf")
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
