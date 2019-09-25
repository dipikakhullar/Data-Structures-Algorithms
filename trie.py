from collections import deque


class TrieNode:
	def __init__(self, v):
		self.val = v
		self.children = {}
		self.is_end = False


class Trie:
	"""
	1. insert
	2. contains word
	3. return all words with prefix
	4. num entries with that prefix?
	5. delete word
	6. return all words in trie
	"""
	def __init__(self):
		self.root = TrieNode(None)


	def insert(self, word):
		"""
		inserts word in trie 
		"""
		if not word:
			return 
		word = self.normalize_word(word)
		trav = self.root

		for i, char in enumerate(word):
			if char not in trav.children:
				trav.children[char] = TrieNode(char)

			trav = trav.children[char]
		trav.is_end = True

	def contains(self, word):
		trav = self.root
		for char in word:
			if char not in trav.children:
				return False

			trav = trav.children[char]

		return trav.is_end

	def get_all_words(self):
		word_list = []
		for letter in self.root.children:
			word_list.extend(self.get_possible_words(letter))
		return word_list



	def longest_prefix(self, word):
		"""
		Finds the word in the trie rooted at root with the longest matching prefix with word.
		In the case of a tie in longest prefix, one word is chosen arbitrarily.

		"""

		current_node = self.root
		current_prefix = ""
		for char in word:
			if char not in current_node.children:
				break
			else:
				current_node = current_node.children[char]
				current_prefix += char

		strings = []
		self.find_strings(current_prefix, current_node, strings)
		return strings[0]

	def find_strings(self, prefix, node, results):
		"""
		Recursively traverses the sub-trie rooted at node and adds all strings of the sub-tree into results.
		"""
		if node.is_end:
			results.append(prefix)
		for char in node.children:
			self.find_strings(prefix + char, node.children[char], results)
		# return results

	def normalize_word(self, word):
		return word.strip().lower()

	def _get_possible_words(self, word, word_node, word_list=None):
		if word_list is None:
			word_list = []
		else:
			word_list

		if word_node.is_end:
			word_list.append(word)
		for letter in word_node.children:
			if not word_node.children[letter]:
				word_list.append(word + letter)
			else:
				self._get_possible_words(word + letter, word_node.children[letter], word_list)
		return word_list

	def get_possible_words(self, word):
		found_prefix = self.found_prefix(word)
		if found_prefix:
			word_node = self._contains(word, self.root) 
			if word_node is None:
				return []
			else:
				return self._get_possible_words(word, word_node)
		else:
			return []

	def found_prefix(self, prefix):
		# found_prefix = True
		current_node = self.root
		found_prefix = True
		for symbol in prefix.strip().lower():
			if symbol in current_node.children:
				current_node = current_node.children[symbol]
			else:
				found_prefix = False 
				break
		return found_prefix


	def _contains(self, word, node):
		if not word:
			return node
		if word[0] and node.children.keys():
			return self._contains(word[1:], node.children[word[0]])
		else:
			return None

	def _contains_word(self, item):
	    current_node = self.root
	    contained = True
	    for symbol in self.normalize_word(item):
	        if symbol in current_node.children:
	            current_node = current_node.children[symbol]
	        else:
	            contained = False
	            break
	    return contained and current_node.is_end
	
	def delete_word(self, word):
		print("DELETING WORD: ", word)
		if self.contains(word):
			word_node = self._contains(word, self.root)
			word_node.is_end = False


trie = Trie()
a = trie.insert("fun")
b = trie.insert("funny")
c = trie.insert("funcakes")
# d = trie.contains("funn")
# print(a)
# print(d)
# trie.longest_prefix("a")
# trie.find_strings("", trie.root, [])
# print("FINDING ALL WORDS")
# words = trie.get_all_words()
# print(words)
all_possible_words = trie.get_possible_words("fu")
print("ALL POSSIBLE WORDS WITH PREFIX FU:  ", all_possible_words)


# # trie.insert("a")
# # trie.insert("add")
# # trie.insert("an")
# # trie.insert("and")
# # trie.insert("any")
# # trie.insert("bagel")
# # trie.insert("bag")
# # trie.insert("bags")
# # trie.insert("bat")
# # trie.insert("bath")
# # trie.insert("bay")
# # prefix = 'z'
# # actual_words = trie.get_possible_words(prefix)
# # print(actual_words)



# t = Trie()
# t.insert("e-mail")
# t.insert("above-said")
# t.insert("above-water")
# t.insert("above-written")
# t.insert("above")
# t.insert("abode")
# t.insert("exit")
# all_words = t.get_all_words()
# # print(all_words)
# # print(all_words)
# # print(len(all_words))
# print(all_words)
# print(t.contains("abode"))
# print(t.contains("above"))
# print(t.contains("above-said"))
# t.delete_word("abode")
# print(t.get_all_words())



