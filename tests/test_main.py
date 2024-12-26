"""
File name: test_main.py
Description: Unit tests for the functionalities in main.py.
Author: Andrey Estevam Seabra
"""

import unittest
import sys
import os

# Imports main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import load_dictionary

class TestMain(unittest.TestCase):

    def test_load_dictionary(self):
        word_dictionary = load_dictionary()
        self.assertIn("dog", word_dictionary.give_suggestions("dog"))
        self.assertIsNotNone(word_dictionary)
        suggestions = word_dictionary.give_suggestions("ban")
        self.assertIn("banana", suggestions)

if __name__ == '__main__':
    unittest.main()