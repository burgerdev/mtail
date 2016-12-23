import unittest

from mtail.re2pred import re2pred


class TestRe2Pred(unittest.TestCase):
    def test_re2pred(self):
        regex = "^asdf$"
        predicate = re2pred(regex)

        assert predicate("asdf")
        assert not predicate("asdfg")
        assert not predicate("0asdf")
        assert not predicate("ghjk")
        
