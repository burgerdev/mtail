import unittest

from mtail.separation import separate


class TestSeparation(unittest.TestCase):
    def test_separate_simple(self):
        stream = ["asdf\n", "ghjk\n"]
        hints = [lambda x: "as" in x, lambda x: "gh" in x]
        out = separate(iter(stream), hints)
        out = list(map(list, out))
        self.assertEqual(len(out), len(stream))
        self.assertEqual(out, [["asdf\n", None], [None, "ghjk\n"]])

    def test_separate_nonexclusive(self):
        stream = ["asdf\n", "ghjk\n"]
        hints = [lambda x: True, lambda x: True]
        out = separate(iter(stream), hints)
        out = list(map(list, out))
        self.assertEqual(len(out), len(stream))
        self.assertEqual(out, [["asdf\n", "asdf\n"], ["ghjk\n", "ghjk\n"]])
