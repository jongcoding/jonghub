import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# 데이터 생성
omega_1 = np.transpose(np.array([[180, 78], [167, 72], [170, 66], [178, 80]]))  # 남자
omega_2 = np.transpose(np.array([[160, 48], [155, 45], [167, 55], [158, 60]]))  # 여자
X = np.hstack([omega_1, omega_2])
y = np.array([0] * len(omega_1) + [1] * len(omega_2))

# 테스트 샘플
x = np.transpose(np.array([165, 65]))  

# 각 클래스에 대한 사전 확률 계산
prior_omega_1 = len(omega_1) / len(X)
prior_omega_2 = len(omega_2) / len(X)

# 각 클래스에 대한 평균과 공분산 추정
mean_omega_1 = np.mean(omega_1, axis=1)
mean_omega_2 = np.mean(omega_2, axis=1)
cov_omega_1 = np.cov(omega_1)
cov_omega_2 = np.cov(omega_2)

# 다변수 정규분포를 사용하여 조건부 확률밀도함수 추정
pdf_omega_1 = multivariate_normal(mean=mean_omega_1, cov=cov_omega_1)
pdf_omega_2 = multivariate_normal(mean=mean_omega_2, cov=cov_omega_2)

0# 테스트 샘플의 사후 확률 계산
posterior_omega_1 = prior_omega_1 * pdf_omega_1.pdf(x)
posterior_omega_2 = prior_omega_2 * pdf_omega_2.pdf(x)

# 클래스 판별
predicted_class = 0 if posterior_omega_1 > posterior_omega_2 else 1

# 시각화
plt.figure(figsize=(8, 6))

# 남자와 여자 클래스 데이터 시각화
plt.scatter(omega_1[:, 0], omega_1[:, 1], color='blue', label='Male')
plt.scatter(omega_2[:, 0], omega_2[:, 1], color='red', label='Female')

# 테스트 샘플 시각화
plt.scatter(x[0], x[1], color='green', marker='x', label='Test Sample')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Bayesian Classifier with Minimum Error')
plt.legend()
plt.grid(True)
plt.show()

# 결과 출력
if predicted_class == 0:
    print("테스트 샘플은 남자에 속합니다.")
else:
    print("테스트 샘플은 여자에 속합니다.")