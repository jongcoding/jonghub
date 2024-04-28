import numpy as np
import matplotlib.pyplot as plt

omega_1 = np.transpose(np.array([[148,72],[183,64],[137,40],[126,60]]))
omega_2 = np.transpose(np.array([[85,66],[89,66],[101,76],[93,70]]))

y_omega1 = np.array([0, 0, 0, 0])
y_omega2 = np.array([1, 1, 1, 1])

omega1_mean = omega_1.mean(axis=1)
omega1_var = np.cov(omega_1, ddof=0)

omega2_mean = omega_2.mean(axis=1)
omega2_var = np.cov(omega_2, ddof=0)

print('mu_1=', omega1_mean)
print('mu_2=', omega2_mean)

print('Sigma_1=\n', omega1_var)
print('Sigma_2=\n', omega2_var)
print('\n')

inv_Sigma1 = np.linalg.inv(omega1_var)
inv_Sigma2 = np.linalg.inv(omega2_var)

coef1_for_g1 = - 1/2 * inv_Sigma1
coef2_for_g1 = omega1_mean.T @ inv_Sigma1
coef3_for_g1 = - 1/2 * omega1_mean.T @ inv_Sigma1 @ omega1_mean - 1/2 * np.log(np.linalg.det(omega1_var))

print('coef_1 = \n', coef1_for_g1)
print('coef_2 = \n', coef2_for_g1)
print('coef_3 = \n', coef3_for_g1)

coef1_for_g2 = - 1/2 * inv_Sigma2
coef2_for_g2 = omega2_mean.T@inv_Sigma2
coef3_for_g2 = - 1/2 * omega2_mean.T @ inv_Sigma2 @ omega2_mean - 1/2 * np.log(np.linalg.det(omega2_var))

coef1_for_g12 = coef1_for_g1 - coef1_for_g2
coef2_for_g12 = coef2_for_g1 - coef2_for_g2
coef3_for_g12 = coef3_for_g1 - coef3_for_g2

print('coef_1 = \n', coef1_for_g12)
print('coef_2 =', coef2_for_g12)
print('coef_3 =', coef3_for_g12)

coef3_for_g12_05_05 = coef3_for_g12 + np.log(0.5)-np.log(0.5)

print('coef_3_05_05 =', 4*coef3_for_g12_05_05)
# 주어진 데이터 포인트
x_point = np.array([118, 76])

# g12(x) 결정 함수 값 계산
g12_x = x_point.T @ coef1_for_g12 @ x_point + coef2_for_g12.T @ x_point + coef3_for_g12

# g12(x)의 값과 분류 결과 출력
g12_x, print('ω1') if g12_x > 0 else print('ω2')

# 주어진 데이터 포인트와 각 클래스의 평균 벡터 사이의 유클리디언 거리 계산
distance_to_omega1 = np.linalg.norm(x_point - omega1_mean)
distance_to_omega2 = np.linalg.norm(x_point - omega2_mean)

# 각 클래스까지의 거리와 분류 결과 출력
print("유클리디언 거리 측정")
distance_to_omega1, distance_to_omega2, print('ω1') if distance_to_omega1 < distance_to_omega2 else print('ω2')


