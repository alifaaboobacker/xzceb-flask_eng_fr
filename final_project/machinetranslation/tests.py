import unittest
from translator import english_to_french,french_to_english
class test_module(unittest.Testcase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("How are you"),"Comment allez-vous")
        self.assertEqual(english_to_french("Are you well"),"Vous allez bien")
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Vous allez bien"),"Are you well")
        self.assertEqual(french_to_english("Ça va"),"How is it going")
unittest.main()

