import numpy as np
from sklearn.linear_model import Perceptron

# 훈련 데이터와 레이블 준비
#omega_1 = np.array([[148, 72], [183, 64], [137, 40], [126, 60]]).T
#omega_2 = np.array([[85, 66], [89, 66], [101, 76], [93, 70]]).T
import numpy as np
from sklearn.linear_model import Perceptron

# 훈련 데이터와 레이블 준비
#omega_1 = np.array([[72, 50], [64, 32], [40, 33], [60,47]]).T
#omega_2 = np.array([[66, 31], [66, 21], [76, 63], [70, 23]]).T
omega_1 = np.array([[148, 72, 50], [183, 64, 32], [137, 40,33], [126, 60,47]]).T
omega_2 = np.array([[85, 66,31], [89, 66,21], [101, 76, 63], [93, 70, 23]]).T
import numpy as np
y_omega1 = np.array([0, 0, 0, 0])
y_omega2 = np.array([1, 1, 1, 1])

# 데이터 결합
x_train = np.concatenate((omega_1.T, omega_2.T), axis=0)
y_train = np.concatenate((y_omega1, y_omega2))

# Perceptron 모델 생성 및 훈련
ppn = Perceptron()
ppn.fit(x_train, y_train)

# 테스트 데이터 정의 및 예측
x_test = np.array([[118,76,63]])
y_pred = ppn.predict(x_test)
x2_test= np.array([[101,76,63]])
y2_pred = ppn.predict(x2_test)
# 예측 결과 출력
print('Prediction for perceptron =', y_pred)
print('Prediction for perceptron =', y2_pred)

