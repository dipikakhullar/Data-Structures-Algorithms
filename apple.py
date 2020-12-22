import enchant
import time 
english_dictionary = enchant.Dict("en_US")

"""
To run:
install enchant:
	pip install pyenchant

	If that doesn't work, and you still get an import error, try
	brew update
	brew install enchant

	python [filename.py]

Time Complexity:
We are doing DFS from each node. DFS runtime is O(V+E), in this case V=16, so DFS runtime is O(1).

However, because we are traversing all the sequences, this complicates things a bit and our runtime is no longer constant. 

For each node, we call DFS and they traverse the other 15 nodes, but all 8 branches traverse the other 14 nodes, and all 8 branches traverse the other 13 nodes, and so on. 
This looks a lot like factorial runtime. O(N!)

Optimizations:
1. Using a trie for pruning => check whether our string + candidate adjacent letter 
is a substring of some word (otherwise we do not need explore from that letter)

2. A DP (dynamic programming)version algorithm ( Bellman-Held-Karp algorithm) will have the complexity of O(2^n * n²). 
By reducing the complexity from factorial to exponential, if the size of n is relatively small the problem can be solvable.

Please note: This algorithm runs ~423 seconds. 
"""


def find_words_in_board(board):
	""" outputs a set of all words present in board in accordance to the following rules:

	Words that can be formed by a sequence of adjacent (top, bottom, left, right, diagonal) letters. 
	Words must be 3 or more letters.
	You may move to any of 8 adjacent letters.
	A word should not have multiple instances of the same cell.

	"""

	start_time = time.time()

	all_words = []
	M = len(board)
	N = len(board[0])

	adjacency_map = create_adjacency_map(board, M, N)
	for r in range(M):
		for c in range(N):
			start_node = (r,c)
			marked = {start_node}
			words = search_board_dfs(board=board, adjacency_map=adjacency_map, string=board[r][c], marked=marked, start_node=start_node)
			all_words.extend(words)
	print("--- %s seconds to execute ---" % (time.time() - start_time))
	return set(all_words)

def search_board_dfs(board, adjacency_map, string, marked, start_node):
	"""
	We will search the board by doing dfs from each node. We will copy a marked set so all paths from start_node are considered.

	For example, with this board:
		board = [
			["R", "A", "E", "L"],
			["M", "O","F", "S"],
			["T", "E", "O", "K"],
			["N", "A", "T", "I"]
		]

	We want to ensure we traverse "SKIT" and "SOT"
	"""
	new_words = []
	if is_word(string):
		print("word found!  ", string)
		new_words.append(string)

	for neighbor in adjacency_map[start_node]:
		if neighbor not in marked:
			row = neighbor[0]
			column = neighbor[1]
			new_string = string + board[row][column]
			new_marked = marked.copy()
			new_marked.add(neighbor)
			new_words = new_words + search_board_dfs(board, adjacency_map, new_string, new_marked, neighbor)
	return new_words

def create_adjacency_map(board, M, N):
	"""Creates an adjacency map where the keys are the nodes, and the values are the nodes nieghbors"""

	adjacency_map = {}
	for r in range(M):
		for c in range(N):
			node = (r,c)
			neighbors = get_neighbors(r, c, M, N)
			adjacency_map[node] = neighbors
	return adjacency_map

def get_neighbors(i, j, M, N):
	"""There are 8 possible neighbors (top, bottom, left, right, diagonal). 
	Returns a map with keys as nodes as tuples (row,column) and all valid neighbors as values.
	"""
	possible_neighbors = [(i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
	valid_neighbors = []

	for x,y in possible_neighbors:
		if 0 <= x <= M-1 and 0 <= y <= N-1:
			node = (x,y)
			valid_neighbors.append(node)
	return valid_neighbors



def is_word(word):
	''' Naive implementation: We import an english dictionary and check for a word's presence
	with the added check that the word must be >= 3 letters long. 

	As per the spec: 
	To check if a string is a valid word you may implement a naive dictionary solution for simplicity
	
	'''

	return len(word) >= 3 and english_dictionary.check(word)


#Let's run our code with some examples
board = [
	["R", "A", "E", "L"],
	["M", "O","F", "S"],
	["T", "E", "O", "K"],
	["N", "A", "T", "I"]
]
words = find_words_in_board(board)
print(words)

