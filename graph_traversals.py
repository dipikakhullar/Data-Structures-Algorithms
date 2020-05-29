import queue

def DFS_recursive(edges_list, start_node):
	adjacency_map = create_adjacency_map(edges_list)
	marked = set()
	helper(start_node, adjacency_map, marked)


def helper(start_node, adjacency_map, marked):
	# print(start_node)
	# print(node)
	marked.add(start_node)
	for node in adjacency_map[start_node]:
		if node not in marked:
			helper(node, adjacency_map, marked)
			# print(node)
	print(start_node)

def create_adjacency_map(edges_list):
	adjacency_map = {}
	for i in edges_list:
		if i[0] in adjacency_map:
			adjacency_map[i[0]].append(i[1])
		else:
			adjacency_map[i[0]] = [i[1]]

		if i[1] in adjacency_map:
			adjacency_map[i[1]].append(i[1])
		else:
			adjacency_map[i[1]] = [i[0]]
	return adjacency_map


edges_list = [["D", "B"], ["D", "F"], ["B", "A"], ["B", "C"], ["F", "E"], ["F", "E"], ["F", "G"]]
start_node = "D"
print("DFS RECURSIVE")
DFS_recursive(edges_list, start_node)
print("done")

def DFS_iterative(edges_list, start_node):
	adjacency_map = create_adjacency_map(edges_list)
	marked = set()
	fringe = []
	fringe.append(start_node)
	marked.add(start_node)
	while fringe:
		node = fringe.pop()
		# print(node)
		# marked.add(start_node)


		# if node not in marked:
		print(node)
		# marked.add(node)
		for neighbors in adjacency_map[node]:
			if neighbors not in marked:
				fringe.append(neighbors)
				marked.add(neighbors)
		# marked.add(node)
		# print(node)

print("DFS ITERATIVE")
DFS_iterative(edges_list, start_node)
print("done")


def BFS_iterative(edges_list, start_node):
	adjacency_map = create_adjacency_map(edges_list)
	marked = set()
	fringe = queue.Queue()
	fringe.put(start_node)
	marked.add(start_node)

	while not fringe.empty():
		node = fringe.get()
		print(node)

		for neighbors in adjacency_map[node]:
			if neighbors not in marked:
				fringe.put(neighbors)
				marked.add(neighbors)

print("BFS ITERATIVE")
BFS_iterative(edges_list, start_node)
print("done")


def BFS_iterative_distance_from_source(edges_list, start_node):
	print('HELLO')
	adjacency_map = create_adjacency_map(edges_list)
	marked = set()
	fringe = queue.Queue()
	fringe.put((start_node, 0))
	marked.add(start_node)

	print("a")
	while not fringe.empty():
		print('b')
		node, distance = fringe.get()
		print("node, distance")
		print(node, distance)
		print(node)

		for neighbors in adjacency_map[node]:
			if neighbors not in marked:
				distance_from_source = distance + 1
				fringe.put((neighbors,distance_from_source))
				marked.add(neighbors)
				if neighbors == 'A':
					return distance_from_source

print("BFS ITERATIVE WITH DISTANCE")
distance = BFS_iterative_distance_from_source(edges_list, start_node)
print("DISTANCE FROM SOURCE: ", distance)
print("done")




def TOPOLOGICAL_SORT(edges_list):
	print("TOPOLOGICAL SORT")
	adjacency_map = create_adjacency_map(edges_list)
	marked = set()
	reverse_postorder = []

	for node in adjacency_map:
		# print(node)
		if node not in marked:
			dfs(adjacency_map, node, marked, reverse_postorder)
	print(reverse_postorder)


def dfs(adjacency_map, start_node, marked, reverse_postorder):
	marked.add(start_node)
	# print(adjacency_map[start_node])
	for neighbor in adjacency_map[start_node]:
		if neighbor not in marked:
			dfs(adjacency_map, neighbor, marked, reverse_postorder)
	reverse_postorder.append(start_node)




TOPOLOGICAL_SORT(edges_list)


def is_cyclic(edges_list):
	"""
	This visits each vertex at most once, and considers each edge at most once, so its runtime is 𝑂(𝑉+𝐸).
	"""
	adjacency_map = create_adjacency_map(edges_list)
	visited = set()
	path = set()
	print(path)
	def visit(vertex):

		if vertex in visited:
			return False
		visited.add(vertex)
		path.add(vertex)

		for neighbor in adjacency_map[vertex]:
			if neighbor in path or visit(neighbor):
				return True
		print(path)
		path.remove(vertex)
		return False

	return any(visit(v) for v in adjacency_map)


print("IS CYCLIC")
is_cycle = is_cyclic(edges_list)
print(is_cycle)




