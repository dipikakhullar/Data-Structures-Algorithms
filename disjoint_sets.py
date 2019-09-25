class DisjointSet: #Weighted Quick Union Disjoint Set with Path Compression
	def __init__(self, N):

		#this id's each node's parent
		self.parent = []

		#this id's each connected component's size
		self.size = []
		for i in range(N):
			self.parent.append(i)
			self.size.append(1)


	def find(self, p):
		if p  == self.parent[p]:
			return p
		else:
			self.parent[p] = self.find(self.parent[p])
			return self.parent[p]

	def is_connected(self, p, q):
		return self.find(p) == self.find(q)

	def connect(self, p, q):
		i = self.find(p)
		j = self.find(q)
		if (i ==j):
			return
		if self.size[i] < self.size[j]:
			self.parent[i] =j
			self.size[j] += self.size[i]
		else:
			self.parent[j] = i
			self.size[i] += self.size[j]


disjoint_set = DisjointSet(14)
print("INITIAL PARENT   :   ", disjoint_set.parent)
print("INITIAL SIZE     :   ", disjoint_set.size)
disjoint_set.connect(0,1)
disjoint_set.connect(11,12)
disjoint_set.connect(12,13)
print(disjoint_set.parent)
print(disjoint_set.size)

for i in range(2,10):
	disjoint_set.connect(1, i)

disjoint_set.connect(11,3)
print(disjoint_set.is_connected(11,2))
print(disjoint_set.parent)
print(disjoint_set.size)
