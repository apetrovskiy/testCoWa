from unittest import TestCase
import unittest

from src.main.java.training.katas.narcissistic.code import narcissistic


class NarcissisticTest(TestCase):
    def test_7(self):
        self.assertEqual(narcissistic(7), True)

    def test_371(self):
        self.assertEqual(narcissistic(371), True)

    def test_122(self):
        self.assertEqual(narcissistic(122), False)

    def test_4887(self):
        self.assertEqual(narcissistic(4887), False)


if __name__ == "__main__":
    unittest.main()
