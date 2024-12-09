import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

encoding_dim = 32

#함수형 api로 신경망 구성
input_img=tf.keras.layers.Input(shape=(784,))
encoded=tf.keras.layers.Dense(encoding_dim, activation='relu')(input_img)
decoded=tf.keras.layers.Dense(784, activation='sigmoid')(encoded)
autoencoder=tf.keras.models.Model(input_img, decoded)

autoencoder.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError())

mnist=tf.keras.datasets.mnist
(x_train, _), (x_test, _)=mnist.load_data()
x_train=x_train.astype('float32') /255.
x_test=x_test.astype('float32') / 255.
x_train=x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test=x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

autoencoder.fit(x_train, x_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test)
                )
dedoced_imgs=autoencoder.predict(x_test)
n=10
plt.figure(figsize=(20,6))
for i in range(1, n+1):
    ax=plt.subplot(2,n,i)
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')

    ax=plt.subplot(2,n,i+n)
    plt.imshow(dedoced_imgs[i].reshape(28,28), cmap='gray')
plt.show()