class Document:
	def __init__(self, title, body):
		self.title = title
		self.body = body

class Solution:
	def autocomplete_scores(self, documents, input_word):
		word_score_map = self.create_word_score_map(documents)
		trie = Trie()
		for word in word_score_map:
			trie.insert(word)
		all_possible_words = trie.get_possible_words(input_word)
		max_score = 0
		for w in all_possible_words:
			if word_score_map[w] > max_score:
				max_score = word_score_map[w]
		return max_score


	def create_word_score_map(self, documents):
		output ={}
		for document in documents:
			title = document.title
			body = document.body
			self.update_word_map(title, output, score = 10)
			self.update_word_map(body, output, score = 1)
		return output

	def update_word_map(self, words, word_map, score = 0):
		local_word = ""
		for i in range(len(words)):
			character = words[i]
			if character == " ":
				if local_word in word_map:
					word_map[local_word] += score
				else:
					word_map[local_word] = score 			
				local_word = ""
			
			else:
				local_word += character
		if local_word in word_map:
			word_map[local_word] += score
		else:
			word_map[local_word] = score 
		return word_map

class TrieNode:
	def __init__(self, v):

		self.value = v
		self.children = {}
		self.is_end = False

class Trie:
	def __init__(self):
		self.root = TrieNode(None)

	def insert(self, word):

		if not word:
			return
		trav = self.root
		# word = self.normalize_word(word)

		for i, char in enumerate(word):
			if char not in trav.children:
				trav.children[char] = TrieNode(char)

			trav = trav.children[char]
		trav.is_end = True

	def _get_possible_words(self, word, word_node, word_list= None):
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
		print(word, found_prefix)

		if found_prefix:
			word_node = self._contains(word, self.root)
			print(word_node.children)
			if word_node is None:
				return []
			else:
				return self._get_possible_words(word, word_node)
		else:
			return []

	def found_prefix(self, prefix):
		current_node = self.root
		found_prefix = True
		for symbol in prefix:
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

	def normalize_word(self, word):
		return word.strip().lower()

	def contains(self, word):
		trav = self.root
		for char in word:
			if char not in trav.children:
				return False

			trav = trav.children[char]

		return trav.is_end

	# def new_search(self, word):
 #        node = self
 #        for w in word:
 #            if w in node.children:
 #                node = node.children[w]
 #            else:
 #                return []
 #        # prefix match
 #        # traverse currnt node to all leaf nodes
 #        result = []
 #        self.new_traverse(node, list(word), result)
 #        return [''.join(r) for r in result]

 #    def new_traverse(self, root, prefix, result):
 #        if root.isEnd:
 #            result.append(prefix[:])
 #        for c,n in root.children.items():
 #            prefix.append(c)
 #            self.new_traverse(n, prefix, result)
 #            prefix.pop(-1)

trie = Trie()
# a = trie.insert("fun")
b = trie.insert("funny")
c = trie.insert("funcakes")
print(trie.contains("funcakes"))
all_possible_words = trie.get_possible_words("fu")
print("ALL POSSIBLE WORDS WITH PREFIX FU:  ", all_possible_words)

document_a = Document("ANIMALS", "ANT ANTELOPE CAMEL CAT DOG")
document_b = Document("DOG FACTS", "FURRY FURRY LOYAL")
documents = [document_a, document_b]

solution = Solution()
an_example = solution.autocomplete_scores(documents, 'AN')
print(an_example)
ELEPH_example = solution.autocomplete_scores(documents, 'ELEPH')
print(ELEPH_example)
FUR_example = solution.autocomplete_scores(documents, 'FUR')
print(FUR_example)








