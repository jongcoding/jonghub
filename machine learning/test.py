import numpy as np
from scipy.spatial.distance import mahalanobis

# 훈련 샘플
w1 = np.array([[180, 78], [167, 72], [170, 66], [178, 80]]) 
w2 = np.array([[160, 48], [155, 45], [167, 55], [158, 60]])

# 평균 벡터 계산
mean_w1 = np.mean(w1, axis=0)
mean_w2 = np.mean(w2, axis=0)

# 공분산 계산
cov_w1 = np.cov(w1.T)
cov_w2 = np.cov(w2.T)

# 사전확률
p_w1 = 0.5
p_w2 = 0.5

# 테스트 샘플
test_sample = np.array([165, 65])

# 마할라노비스 거리 계산
dist_w1 = mahalanobis(test_sample, mean_w1, np.linalg.inv(cov_w1))
dist_w2 = mahalanobis(test_sample, mean_w2, np.linalg.inv(cov_w2))

# 사후확률 계산
p_w1_given_x = p_w1 * np.exp(-0.5 * dist_w1) / (p_w1 * np.exp(-0.5 * dist_w1) + p_w2 * np.exp(-0.5 * dist_w2))
p_w2_given_x = p_w2 * np.exp(-0.5 * dist_w2) / (p_w1 * np.exp(-0.5 * dist_w1) + p_w2 * np.exp(-0.5 * dist_w2))

# 분류 결과
if p_w1_given_x > p_w2_given_x:
    print("테스트 샘플 (165, 65)T는 w1 클래스(남자)에 속합니다.")
else:
    print("테스트 샘플 (165, 65)T는 w2 클래스(여자)에 속합니다.")