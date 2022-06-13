#%%

# numpy:

import numpy as np
import numpy.linalg as linalg

# matplotlib:

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

#%%
# vom grupa elevii unor clase despre care cunoaștem mediile la română, matematică și engleză:
note_elevi = np.array([
    [8, 7, 7],
    [9, 9, 9],
    [9, 9, 8],
    [6, 6, 8],
    [9, 7, 7],
    [7, 7, 7],
    [4, 4, 4],
    [5, 6, 8],
    [7, 6, 6],
    [4, 4, 4],
    [9, 10, 9],
    [10, 9, 9],
    [6, 6, 7],
    [7, 8, 5],
    [5, 5, 9],
    [3, 3, 3],
    [8, 8, 8],
    [6, 10, 9],
    [6, 8, 8],
    [9, 9, 9],
    [5, 6, 7],
    [2, 3, 3],
    [5, 7, 8],
    [4, 7, 4],
    [6, 6, 5],
])

def euclidian_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Pasul 1 - alegem k = numărul de grupuri
k = 4

# Pasul 2 - alegem k indici din vector
indices = list(range(len(note_elevi)))
np.random.shuffle(indices)
centroids = [note_elevi[i] for i in indices[0:k]]

# calculam care indici sunt cei mai apropiati de fiecare centroid in parte

print(centroids)

for _ in range(100):
    groups = [[] for _ in range(k)]
    for note_elev in note_elevi:
        distances = [euclidian_distance(centroid, note_elev) for centroid in centroids]
        min_idx = 0
        min_distance = distances[0]
        for idx2, distance in enumerate(distances):
            if distance < min_distance:
                min_idx, min_distance = idx2, distance
        # print(min_idx, min_distance, distances)
        groups[min_idx].append(note_elev)

    centroids = [np.asarray(np.matrix(group).mean(0))[0] for group in groups]
    # print('centroids:', *centroids, sep='\n')

# Pasul 4
# folosim centroizii pentru a clasifica
#%%
groups = [[] for _ in range(k)]
for i, note_elev in enumerate(note_elevi):
    distances = [euclidian_distance(centroid, note_elev) for centroid in centroids]
    min_idx = 0
    min_distance = distances[0]
    for idx2, distance in enumerate(distances):
        if distance < min_distance:
            min_idx, min_distance = idx2, distance
    # print(min_idx, min_distance, distances)
    groups[min_idx].append(i)
print(*groups, sep='\n')
color_of = {}
for group_id in range(len(groups)):
    for i in groups[group_id]:
        color_of[i] = group_id
print(color_of)

#%%
fig = plt.figure()
ax: Axes3D = fig.add_subplot(projection='3d')

colors = ['red', 'forestgreen', 'royalblue', 'orange', 'black']

ax.scatter3D(*note_elevi.T, c=[colors[color_of[i]] for i in range(len(note_elevi))])
ax.set_xlabel('Note Romana')
ax.set_ylabel('Note Mate')
ax.set_zlabel('Note Engleza ')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

for i, centroid in enumerate(centroids):
    for point_idx in groups[i]:
        point = note_elevi[point_idx]
        ax.plot(*zip(point, centroid), color=colors[i])

fig.show()
#%%
# # num_pupils = 25
# # grades = []
# #
# # means = np.array([np.random.normal() for _ in range(num_pupils)])
# # if means.min() < 0:
# #     means -= means.min()
# # means *= 10 / means.max()
# #
# # print(np.ceil(means))
# # means[means < 5] += 2
# # print(np.ceil(means))
#
# means = [7, 10, 7, 7, 8, 6, 6, 7, 7, 4,
#          10, 10, 6, 6, 7, 5, 8, 8, 7, 8,
#          7, 2, 7, 6, 6]
#
# for mean in means:
#     # difference of 2:
#     low = mean - np.random.randint(0, 3)
#     if high < 1:
#         high = 1
#     high = mean + np.random.randint(0, 3)
#     if high > 10:
#         high = 10
#
#     print(np.random.random_integers(low, high, 3))
#
# np.random.random_integers(low, high)