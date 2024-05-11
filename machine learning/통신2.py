import numpy as np
import matplotlib.pyplot as plt
# 시간 범위를 넓혀서 재구성 (0.05초까지 확장)
t = np.linspace(-0.1, 0.1, 2000)

# 주어진 메시지 신호 m(t)
m_t = 2 * np.cos(200 * t) + 3 * np.cos(300 * t)

# 힐버트 변환된 메시지 신호
m_hat_t = 2 * np.sin(200 * t) + 3 * np.sin(300 * t)

# 반송파 주파수
omega_c = 1000

# SSB-SC 신호 재계산
phi_SSB_t = (2 * np.cos(200 * t) + 3 * np.cos(300 * t)) * np.cos(omega_c * t) - (2 * np.sin(200 * t) + 3 * np.sin(300 * t)) * np.sin(omega_c * t)

# 시각화
plt.figure(figsize=(12, 8))

plt.subplot(211)
plt.plot(t, m_t, label='m(t) = 2cos(200t) + 3cos(300t)')
plt.title('Extended View: Message Signal m(t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(212)
plt.plot(t, phi_SSB_t, label='phi_SSB(t)')
plt.title('Extended View: SSB-SC Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
