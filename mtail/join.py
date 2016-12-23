
from functools import partial

def _apply_format(fmt_string, items):
    return "".join(map(mapper, items)) + "\n"


def join(stream, width):
    width = int(width)
    fmt_string = "{:" + str(width) + "s}"

    def mapper(item):
        if item is None:
            item = ""
        return fmt_string.format(item.rstrip())[:width]

    for items in stream:
        yield "".join(map(mapper, items)) + "\n"
