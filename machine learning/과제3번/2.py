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

# 계층적 클러스터링 (완전 연결법)
linkage_complete = linkage(data, method='complete')

# 덴드로그램 그리기
plt.figure(figsize=(10, 7))
dendrogram(linkage_complete)
plt.title("Dendrogram (Complete Linkage)")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.show()

# 3개의 군집으로 나누기
cluster_complete = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='complete')
y_complete = cluster_complete.fit_predict(data)

print("Clusters (Complete Linkage):", y_complete)

# 클러스터링 결과 시각화
plt.title("Clustering with Complete Linkage")
colors = ['ro', 'bs', 'g^']
for i in range(3):
    plt.plot(data[y_complete == i, 0], data[y_complete == i, 1], colors[i])
plt.xlabel("x1 (크기)")
plt.ylabel("x2 (귀의 길이)")
plt.grid(True)
plt.show()
