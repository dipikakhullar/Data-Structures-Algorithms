
class BSTNode:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None


def pre_order(root):
	if root == None:
		return
	else: 
		print(root.value)
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root == None:
		return
	else:
		in_order(root.left)
		print(root.value)
		in_order(root.right)


def post_order(root):
	if root == None:
		return
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.value)


def insert(root, key):
	if root == None:
		return BSTNode(key)
	elif key < root.value:
		root.left = insert(root.left, key)

	elif key >= root.value:
		root.right = insert(root.right, key)
	return root

# def print_BST(root):
	# if root == None

BST = insert(None, "D")
insert(BST, "A")
insert(BST, "B")
insert(BST, "C")
insert(BST, "E")
insert(BST, "F")
insert(BST, "G")
print(BST)
print("PREORDER:   ")
pre_order(BST)
print("INORDER:    ")
in_order(BST)
print("POSTORDER:  ")
post_order(BST)
