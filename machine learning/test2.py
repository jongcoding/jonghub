# 수정된 전체 코드 실행
import numpy as np
import matplotlib.pyplot as plt
# 데이터 생성
omega_1 = np.array([[1, 2], [3, 1], [5, 2], [3, 3]])  # 클래스 1
omega_2 = np.array([[7, 6], [8, 4], [9, 6], [8, 8]])  # 클래스 2

# 클래스별 평균 벡터 계산
omega1_mean = np.mean(omega_1, axis=0)
omega2_mean = np.mean(omega_2, axis=0)

# 클래스별 공분산 행렬 계산 및 역행렬 계산
omega1_cov = np.cov(omega_1.T)
inv_omega1_cov = np.linalg.inv(omega1_cov)

omega2_cov = np.cov(omega_2.T)
inv_omega2_cov = np.linalg.inv(omega2_cov)

# 계수 계산
coef1_for_g1 = -0.5 * inv_omega1_cov
coef2_for_g1 = inv_omega1_cov @ omega1_mean
coef3_for_g1 = -0.5 * (omega1_mean.T @ inv_omega1_cov @ omega1_mean + np.log(np.linalg.det(omega1_cov)))

coef1_for_g2 = -0.5 * inv_omega2_cov
coef2_for_g2 = inv_omega2_cov @ omega2_mean
coef3_for_g2 = -0.5 * (omega2_mean.T @ inv_omega2_cov @ omega2_mean + np.log(np.linalg.det(omega2_cov)))

# 결정 경계 계수
coef1_for_g12 = coef1_for_g1 - coef1_for_g2
coef2_for_g12 = coef2_for_g1 - coef2_for_g2
coef3_for_g12 = coef3_for_g1 - coef3_for_g2

# 결정 경계 시각화
x_min, x_max = 0, 10
y_min, y_max = 0, 10
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

# 결정 함수
def decision_function(x, y, coef1, coef2, coef3):
    xy = np.array([x, y])
    return np.dot(xy.T, np.dot(coef1, xy)) + np.dot(coef2, xy) + coef3

# 결정 경계 생성
Z = np.array([decision_function(x, y, coef1_for_g12, coef2_for_g12, coef3_for_g12) for x, y in zip(np.ravel(xx), np.ravel(yy))])
Z = Z.reshape(xx.shape)

# 데이터 및 결정 경계 시각화
plt.figure(figsize=(8, 6))
plt.plot(omega_1[:, 0], omega_1[:, 1], 'ro', label='Class 1')
plt.plot(omega_2[:, 0], omega_2[:, 1], 'bo', label='Class 2')
plt.contour(xx, yy, Z, levels=[0], colors='green')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Decision Boundary between Class 1 and Class 2')
plt.legend()
plt.grid(True)
plt.show()
