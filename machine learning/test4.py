import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
omega_1 = np.transpose(np.array([[180, 78], [167, 72], [170, 66], [178, 80]])) # 남자
omega_2 = np.transpose(np.array([[160, 48], [155, 45], [167, 55], [158, 60]])) # 여자
X = np.hstack([omega_1, omega_2])
y = np.array([0] * len(omega_1) + [1] * len(omega_2))

# 테스트 샘플
x = np.transpose(np.array([165, 65]))

# 클래스별 평균 벡터 계산
mean_omega_1 = np.mean(omega_1, axis=1)
mean_omega_2 = np.mean(omega_2, axis=1)

# 클래스별 공분산 행렬 계산
cov_omega_1 = np.cov(omega_1)
cov_omega_2 = np.cov(omega_2)

# 역 공분산 행렬 계산
inv_cov_omega_1 = np.linalg.inv(cov_omega_1)
inv_cov_omega_2 = np.linalg.inv(cov_omega_2)

# 평균 벡터 그리기
plt.plot(mean_omega_1[0], mean_omega_1[1], 'ro', markersize=10, label='Man Class Mean')
plt.plot(mean_omega_2[0], mean_omega_2[1], 'bs', markersize=10, label='Woman Class Mean')

# 테스트 샘플 출력
plt.scatter(x[0], x[1], c='g', label='Test Sample')

# 훈련 데이터 출력
plt.scatter(omega_1[0], omega_1[1], c='r', label='Man')
plt.scatter(omega_2[0], omega_2[1], c='b', label='Woman')

x_min, x_max = X[0].min() - 1, X[0].max() + 1
y_min, y_max = X[1].min() - 1, X[1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

Z = np.zeros(xx.shape)

# 두 평균 벡터를 이어주기
plt.plot([mean_omega_1[0], mean_omega_2[0]], [mean_omega_1[1], mean_omega_2[1]], color='black', linestyle='--')

# Mahalanobis 거리 계산 함수
def mahalanobis_distance(x, mean, inv_covariance):
    x_minus_mean = x - mean
    mahala_dist = np.sqrt(np.dot(np.dot(x_minus_mean.T, inv_covariance), x_minus_mean))
    return mahala_dist

# 남자와 여자의 Mahalanobis 거리 계산 및 결정 경계 그리기
for i in range(len(xx)):
    for j in range(len(yy)):
        point = np.array([xx[i, j], yy[i, j]])
        dist_omega_1 = mahalanobis_distance(point, mean_omega_1, inv_cov_omega_1)
        dist_omega_2 = mahalanobis_distance(point, mean_omega_2, inv_cov_omega_2)
        Z[i, j] = dist_omega_1 - dist_omega_2

plt.contour(xx, yy, Z, levels=[0], colors='green')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Decision Boundary with Mahalanobis Distance')
plt.legend()
plt.grid(True)
plt.show()

# 남자 클래스와 여자 클래스의 Mahalanobis 거리 계산
Mahala_dist1 = mahalanobis_distance(x, mean_omega_1, inv_cov_omega_1)
Mahala_dist2 = mahalanobis_distance(x, mean_omega_2, inv_cov_omega_2)

# 남자인지 여자인지 결정
if Mahala_dist1 < Mahala_dist2:
    print("테스트 샘플은 남자에 속합니다.")
else:
    print("테스트 샘플은 여자에 속합니다.")