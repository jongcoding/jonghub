import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# 주어진 데이터 정의
data = np.array([
    [30, 10, 20],
    [25, 8, 18],
    [20, 6, 15],
    [15, 5, 12],
    [10, 3, 8],
    [12, 4, 10],
    [18, 7, 14],
    [22, 8, 16]
])

# 거리 행렬 계산
dist_p = squareform(pdist(data, metric='euclidean'))
print(dist_p)
# 계층적 클러스터링 (단일 연결법)
linkage_single = linkage(data, method='single')

# 덴드로그램 그리기
plt.figure(figsize=(10, 7))
dendrogram(linkage_single)
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.show()

# 3개의 군집으로 나누기
cluster_single = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='single')
y_single = cluster_single.fit_predict(data)

print("Clusters (Single Linkage):", y_single)

# 클러스터링 결과 시각화
plt.title("Clustering with Single Linkage")
colors = ['ro', 'bs', 'g^']
for i in range(3):
    plt.plot(data[y_single == i, 0], data[y_single == i, 1], colors[i])
plt.xlabel("x1 (크기)")
plt.ylabel("x2 (귀의 길이)")
plt.grid(True)
plt.show()

