import unittest
from trie import Trie as Trie 
class TestTrie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #            root
        #          /      \
        #       /           \
        #     a *             b
        #    / \             /
        #   d   n *         a
        #  /   / \       /  |  \
        # d * d * y *   g * t *  y *
        #              / \   \
        #             e   s * h *
        #            /
        #           l *
        # asterisk denotes a word

        trie = Trie()
        cls._trie = Trie()
        cls._trie.insert("a")
        cls._trie.insert("add")
        cls._trie.insert("an")
        cls._trie.insert("and")
        cls._trie.insert("any")
        cls._trie.insert("bagel")
        cls._trie.insert("bag")
        cls._trie.insert("bags")
        cls._trie.insert("bat")
        cls._trie.insert("bath")
        cls._trie.insert("bay")

        cls._trie_length = 11 # magic number, the number of words in the trie

    def test(self):
        assert len(self._trie.get_all_words()) == self._trie_length
        all_words = self._trie.get_all_words()

        assert "a" in all_words
        assert "add" in all_words
        assert "an" in all_words
        assert "and" in all_words
        assert "any" in all_words
        assert "bagel" in all_words
        assert "bag" in all_words
        assert "bags" in all_words
        assert "bat" in all_words
        assert "bath" in all_words
        assert "bay" in all_words

    def test_duplicate_entries(self):
        """Adding a word that already exists should not create a new word in the trie"""
        t = self._trie
        t.insert("bag")
        all_words = t.get_all_words()

        assert len(t.get_all_words()) == self._trie_length
        assert "bag" in all_words

    def test_mixed_case(self):
        """insert and retrieval are case insensitive"""
        t = Trie()
        t.insert("APPLE")
        t.insert("oRANge")
        all_words = t.get_all_words()
        
        assert "apple" in all_words
        assert "orange" in all_words

        # assert "APPLE" in all_words
        # assert "ORANGE" in all_words
# 
        # assert "aPpLe" in all_words
        # assert "oRangE" in all_words

    def test_hyphenated_words(self):
        t = Trie()
        t.insert("e-mail")
        t.insert("above-said")
        t.insert("above-water")
        t.insert("above-written")
        t.insert("above")
        t.insert("abode")
        t.insert("exit")
        all_words = t.get_all_words()

        assert len(t.get_all_words()) == 7

        assert "abode" in all_words
        assert "above" in all_words
        assert "above-written" in all_words
        assert "above-water" in all_words
        assert "above-said" in all_words
        assert "e-mail" in all_words
        assert "exit" in all_words

    def test_empty_trie(self):
        t = Trie()
        assert len(t.get_all_words()) == 0

    def test_first_symbol_is_a_word(self):
        t = Trie()
        t.insert("a")
        t.insert("apple")
        all_words = t.get_all_words()

        assert "a" in all_words
        assert "apple" in all_words

        words = t.get_all_words()
        assert len(words) == 2
        assert "a" in words
        assert "apple" in words

    def test_get_possible_words(self):
        prefix = 'an'
        expected_words = ['an', 'and', 'any']
        actual_words = self._trie.get_possible_words(prefix)
        assert len(expected_words) == len(actual_words)
        for word in expected_words:
            assert word in actual_words

        prefix = 'ba'
        expected_words = ["bagel", "bag", "bags", "bat", "bath", "bay"]
        actual_words = self._trie.get_possible_words(prefix)
        assert len(expected_words) == len(actual_words)
        for word in expected_words:
            assert word in actual_words

    def test_get_possible_words_no_more_words(self):
        """test that given a prefix that is a terminus with no children in the trie, returns that one word"""
        prefix = 'any'
        actual_words = self._trie.get_possible_words(prefix)
        assert len(actual_words) == 1
        assert prefix in actual_words

    def test_get_possible_words_prefix_not_in_trie(self):
        prefix = 'z'
        actual_words = self._trie.get_possible_words(prefix)
        assert len(actual_words) == 0









