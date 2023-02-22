import unittest

from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase):
    def test1(self):
        #self.assertEqual(english_to_french(''), '')
        self.assertNotEqual(english_to_french('None'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFr2En(unittest.TestCase):
    def test1(self):
        #self.assertEqual(french_to_english(''), '')
        self.assertNotEqual(french_to_english('None'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()