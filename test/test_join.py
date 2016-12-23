import unittest

from mtail.join import join


class TestJoin(unittest.TestCase):
    def test_join_simple(self):
        data = [["asdf", None], [None, "ghjk"]]
        joined = list(join(iter(data), width=4))
        expected = ["asdf    \n", "    ghjk\n"]
        self.assertEqual(joined, expected)

    def test_join_newline(self):
        data = [["asdf\n", None], [None, "ghjk\n"]]
        joined = list(join(iter(data), width=4))
        expected = ["asdf    \n", "    ghjk\n"]
        self.assertEqual(joined, expected)

    def test_join_max(self):
        data = [["asdf\n", None], [None, "ghjk\n"]]
        joined = list(join(iter(data), width=2))
        expected = ["as  \n", "  gh\n"]
        self.assertEqual(joined, expected)

    def test_format_injection(self):
        pass
