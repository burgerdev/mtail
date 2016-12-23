
from functools import partial

def _apply_clue(clue, item):
    if clue(item):
        return item
    else:
        return None


def separate(stream, clues):
    clue_funcs = list(map(lambda f: partial(_apply_clue, f), clues))
    for line in stream:
        yield map(lambda f: f(line), clue_funcs)
