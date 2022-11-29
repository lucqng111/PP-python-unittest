import unittest
from unittest import TestCase, TestLoader

class TestTest(TestCase):
    def test_func(self):
        self.assertTrue(True)


unittest.main()