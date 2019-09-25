from collections import defaultdict
class Solution(object):

	def ladderLength(self, beginWord, endWord, wordList):
		"""
		NOTES:
		When would you use a default dict? When would you not use a default dict?

		"""
		if endWord not in wordList or not endWord or not beginWord or not wordList:
			return 0

		#We know all words are the same length
		L = len(beginWord)


		#Dictionary to hold combination of words that can be formed, from any given word. By changing on letter at a time. 
		all_combinations_dict = defaultdict(list)

		for word in wordList:
			for i in range(L):

				generic_word = word[:i] + "*" + word[i + 1]
				all_combinations_dict[generic_word].append(word)