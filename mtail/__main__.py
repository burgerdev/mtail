
from .join import join
from .separation import separate
from .re2pred import re2pred

_WIDTH = 20

def main(clues, width):
    import sys
    sep = separate(sys.stdin, clues)
    joined = join(sep, width)

    for line in joined:
        sys.stdout.write(line)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser("TODO")

    parser.add_argument("-w", "--width", type=int, default=_WIDTH,
                        help="column width (default: {})".format(_WIDTH))
    parser.add_argument("res", metavar="regex", nargs="*",
                        help="regular expression for this column")

    args = parser.parse_args()

    clues = map(re2pred, args.res)
    width = args.width

    main(clues, width)
