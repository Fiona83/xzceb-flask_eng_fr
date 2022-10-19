"""
Unittest for translator
"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Unittest class for translator
    """
    def test_english_to_frech(self):
        """
        test cases for english_to_french
        """
        self.assertNotEqual(english_to_french("None"), " ")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_engilsh(self):
        """
        test case for french_to_english
        """
        self.assertNotEqual(french_to_english("None"), " ")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
