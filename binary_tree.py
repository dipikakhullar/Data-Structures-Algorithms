#Definition for a binary tree node.
from queue import Queue
class TreeNode:
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


def level_order_traversal(root):
	#Add root to Queue
	queue = Queue()
	level_nodes = {}
	level = 0
	queue.put(root)

	while not queue.empty():
		num_nodes_level_i = queue.qsize()
		level_nodes[level] = []

		for i in range(num_nodes_level_i):
			node = queue.get()
			print(node.value)
			level_nodes[level].append(node)

			if node.right:
				queue.put(node.right)
			if node.left:
				queue.put(node.left)
		level += 1

	return level_nodes

def top_view(root):
	queue = Queue()
	top_view = []
	queue.put(root)

	while not queue.empty():
		num_nodes_level_i = queue.qsize()

		for i in range(num_nodes_level_i):
			node = queue.get()
			if i == 0 or i == num_nodes_level_i -1:
				top_view.append(node)


			if node.left:
				queue.put(node.left)
			if node.right:
				queue.put(node.right)

	return [node.value for node in top_view]

def sum_each_level(root):
	queue = Queue()
	sum_levels = []

	queue.put(root)
	while not queue.empty():
		num_nodes_level_i = queue.qsize()
		sum_level_i = 0

		for i in range(num_nodes_level_i):
			node = queue.get()
			sum_level_i += node.value

			if node.left:
				queue.put(node.left)
			if node.right:
				queue.put(node.right)

		sum_levels.append(sum_level_i)

	return sum_levels



level_order = level_order_traversal(root)
print("level order map: ", level_order)

top_view = top_view(root)
print("top view: ", top_view)

sum_levels = sum_each_level(root)
print("sum levels: ", sum_levels)















