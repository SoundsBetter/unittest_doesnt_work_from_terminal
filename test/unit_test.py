from unittest import TestCase
from unittest_doesnt_work_from_terminal import data

typical_cases = [
    ('abcd efgh', 'dcba hgfe'),
    ('a1bcd efg!h', 'd1cba hgf!e'),
    ('', '')
]


class AnagramsTest(TestCase):
    def test_typical(self):
        for p1, p2 in typical_cases:
            with self.subTest():
                self.assertEqual(data.anagram(p1), p2)
