import freetype

from . import generators
from . import training


def get_letter(c):
    return generators.char(c)
