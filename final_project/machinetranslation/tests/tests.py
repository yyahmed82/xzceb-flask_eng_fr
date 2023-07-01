import unittest
from translator import english_to_french, french_to_english

class TestEn(unittest.TestCase):
       def test1(self):
        # Tests Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFr(unittest.TestCase):
    def test1(self):
        # Tests Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()