import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage


c1 = np.array([[30, 10, 20], [25, 8, 18], [20, 6, 15], [15, 5, 12]])
c2 = np.array([[10, 3, 8], [12, 4, 10], [18, 7, 14], [22, 8, 16]])


data = np.vstack((c1, c2))


distances = pdist(data)
dist_matrix = squareform(distances)


linkage_single = linkage(data, method='single')  # Dmin
linkage_complete = linkage(data, method='complete')  # Dmax
linkage_average = linkage(data, method='average')  # Davg


Dmin = np.min(linkage_single[:, 2])
Dmax = np.max(linkage_complete[:, 2])
Dave = np.mean(linkage_average[:, 2])


mean_c1 = np.mean(c1, axis=0)
mean_c2 = np.mean(c2, axis=0)


D_mean = np.linalg.norm(mean_c1 - mean_c2)
D_rep = D_mean  

print("Dmax:",Dmax)
print("Dmin:",Dmin)
print("Dave:",Dave)
print("Dmean:",D_mean)
print("Drep:",D_rep)
