import unittest

from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFr2En(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
