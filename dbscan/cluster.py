from time import perf_counter
import keras
import numpy as np
from sklearn import cluster, metrics, decomposition
import matplotlib.pyplot as plt
from skimage import transform

mnist = keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()

# scale images down to 7x7
train_x_small = [transform.rescale(img, 0.25, anti_aliasing=True) for img in train_x]
test_x_small = [transform.rescale(img, 0.25, anti_aliasing=True) for img in test_x]

# flatten image data using list comprehension
train_x_flat = np.array([[item for sublist in image for item in sublist] for image in train_x_small])
test_x_flat = np.array([[item for sublist in image for item in sublist] for image in test_x_small])
# train_x_flat = decomposition.PCA(n_components = 2).fit_transform(train_x_flat)
# test_x_flat = decomposition.PCA(n_components = 2).fit_transform(test_x_flat)

clock = perf_counter()
db = cluster.DBSCAN(eps = 0.5, min_samples = 5, n_jobs=-1).fit(train_x_flat)
print(f"TIME: {perf_counter() - clock}")
labels = db.labels_
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(n_clusters)
print(n_noise)

# plot result
unique_labels = set(labels)
colours = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colours):
    if k == -1:
        # black used for noise
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = train_x_flat[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

    xy = train_x_flat[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)

plt.title(f"{n_clusters} estimated clusters.")
plt.show()
