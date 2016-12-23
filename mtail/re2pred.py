
import re


def re2pred(regex):
    compiled = re.compile(regex)
    def matches(item):
        return compiled.match(item) is not None
    return matches
