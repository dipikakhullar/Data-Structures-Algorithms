
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from matplotlib import style
style.use('ggplot')

class KMeans:
	def __init__(self, k=2, tolerance = 0.001, max_iterations=300):
		self.k = k
		self.tolerance = tolerance
		self.max_iterations = max_iterations


	def euclidean_distance(self, point1, point2):
		# return np.linalg.norm(point1-point2)
		distance = 0
		for i in range(len(point1)):
			distance += (point1[i] - point2[i])**2
		#sqrt of the sum of the squared distnaces at each dimension
		return sqrt(distance)

	def fit(self, data):
		self.centroids = {}

		#randomly assigning the iniital cnetroids
		for i in range(self.k):
			self.centroids[i] = data[i]

		print(self.centroids)
		for i in range(self.max_iterations):
			self.classifications = {}

			for i in range(self.k):
				self.classifications[i] = []

			for point in data:
				distances_from_centroids = [self.euclidean_distance(point, self.centroids[i]) for i in self.centroids]

				#which cluster the point belongs to currently
				classification = distances_from_centroids.index(min(distances_from_centroids))

				self.classifications[classification].append(point)


			#Now we will update our centroids
			previous_centroids = dict(self.centroids)
			for c in self.classifications:
				#new centroids are the average of all the points in the cluster. 
				self.centroids[c] = np.average(self.classifications[c], axis=0)
				opimized = True


			for center in self.centroids:
				original_centroid = previous_centroids[center]
				current_centroid = self.centroids[c]

				if sum((current_centroid - original_centroid)/original_centroid * 100) > self.tolerance:
					print((current_centroid - original_centroid)/original_centroid * 100)
					opimized = False

			if opimized:
				break
	def predict(self, data_point):
		distances = []
		for c in self.centroids:
			distances.append(self.euclidean_distance(c, data_point))
		classification = distances.index(min(distances))
		return classification


X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11]])

# plt.scatter(X[:,0], X[:,1], s=150)
# plt.show()


model = KMeans(k=2)
model.fit(X)

for centroid in model.centroids:
    plt.scatter(model.centroids[centroid][0], model.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in model.classifications:
    # color = colors[classification]
    for featureset in model.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color='black', s=150, linewidths=5)
        
plt.show()


