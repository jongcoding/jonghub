import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

encoding_dim =32
input_img=tf.keras.layers.Input(shape=(784,))
encoded=tf.keras.layers.Dense(encoding_dim, activation='relu')(input_img)
decoded=tf.keras.layers.Dense(784, activation='sigmoid')(encoded)
autoencoder=tf.keras.Model(input_img, decoded)
#함수형 API를 이용하여 신경망 구축

mnist=tf.keras.datasets.mnist

(x_train,_),(x_test,_)=mnist.load_data()
x_train=x_train.astype('float32') /255.
x_test=x_test.astype('float32') /255.
x_train=x_train.reshape(len(x_train), np.prod(x_train.shape[1:]))
x_test=x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
#MNIST 데이터 처리

noise_factor=0.55
original_train=x_train
original_test= x_test
noise_train=np.random.normal(0,1,original_train.shape)
noise_test=np.random.normal(0,1,original_test.shape)
noisy_train=original_train+noise_factor*noise_train
noisy_test=original_test*noise_factor*noise_test
#넘파이 연산을 이용하여 영상에 노이즈를 추가



autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(noisy_train, original_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(noisy_test, original_test))

denoised_images=autoencoder.predict(noisy_test)

#학습 및 예측

n=10
plt.figure(figsize=(20,6))
for i in range(1, n+1):
    ax=plt.subplot(3,n, i)
    plt.imshow(noisy_test[i].reshape(28,28), cmap='gray')
    plt.gray()

    ax=plt.subplot(3, n, i+n)
    plt.imshow(denoised_images[i].reshape(28,28), cmap='gray')
    plt.gray()

    ax=plt.subplot(3,n, i+2*n)
    plt.imshow(original_test[i].reshape(28,28), cmap='gray')
    plt.gray()

plt.show()

#학습 및 예측