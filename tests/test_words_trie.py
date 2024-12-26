"""
File name: test_words_trie.py
Description: Unit tests for the functionalities in words_trie.py.
Author: Andrey Estevam Seabra
"""

import unittest
import sys
import os

# Adds the autocomplete_flask directory to the Python path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../autocomplete_flask')))
import words_trie

class TestTrieWords(unittest.TestCase):
    """
    Unit test class for the TrieWords class in words_trie.py.
    """

    def setUp(self) -> None:
        """
        Initializes a new TrieWords() class before each test.
        """
        self.words = words_trie.TrieWords()
    
    def test_insert_word(self) -> None:
        """
        Tests that words are correctly inserted to the Trie data structure.
        """
        self.words.insert_word("cat")
        self.words.insert_word("catalog")
        self.words.insert_word("call")
        self.words.insert_word("bird")
        self.words.insert_word("red")
        suggestions = self.words.give_suggestions("ca")

        self.assertEqual(["cat", "catalog", "call"], suggestions)
        self.assertNotEqual(["bird"], suggestions)
    
    def test_prefix_search(self) -> None:
        """
        Tests that the method prefix_search() in TrieWords() returns the correct node in the Trie.
        """
        self.words.insert_word("cat")
        self.words.insert_word("catalog")
        prefix_node = self.words.prefix_search("cat")
        
        self.assertEquals(self.words.root.children["c"].children["a"].children["t"], prefix_node)
    
    def test_give_suggestions(self) -> None:
        """
        Tests that the method give_suggestions() gives correct suggestions and handles invalid inputs.
        """
        self.words.insert_word("computer")
        self.words.insert_word("python")
        self.words.insert_word("phone")
        self.words.insert_word("unittest")
        self.words.insert_word("happiness")

        suggestions = self.words.give_suggestions("c")
        self.assertEqual(["computer"], suggestions)
        suggestions_two = self.words.give_suggestions("app")
        self.assertEqual([], suggestions_two)
        suggestions_three = self.words.give_suggestions("")
        self.assertEqual(["computer", "python", "phone", "unittest", "happiness"], suggestions_three)

if __name__ == '__main__':
    unittest.main()