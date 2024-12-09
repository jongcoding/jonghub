import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

# 학습 데이터와 테스트 데이터 분리
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 이미지를 [0, 1] 범위로 스케일링
x_train = x_train.astype("float32") / 255.
x_test = x_test.astype("float32") / 255.

# 입력 데이터 평탄화
BATCH_SIZE = 128
EPOCHS = 2000
Z_DIMENSIONS = 32
data = np.reshape(x_train, (x_train.shape[0], 28, 28, 1))

# 판별자 신경망 구성
def make_discriminator():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(64, (5,5), strides=(2,2), padding='same', activation='relu', input_shape=[28,28,1]))
    model.add(tf.keras.layers.Dropout(0.4))
    model.add(tf.keras.layers.Conv2D(256,(5,5), strides=(2,2), padding='same', activation='relu'))
    model.add(tf.keras.layers.Dropout(0.4))
    model.add(tf.keras.layers.Conv2D(256,(5,5), strides=(2,2), padding='same', activation='relu'))
    model.add(tf.keras.layers.Dropout(0.4))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    return model

discriminator = make_discriminator()
discriminator.compile(
    loss='binary_crossentropy',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0004),
    metrics=['accuracy']
)

def make_generator():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(7*7*64, input_shape=(Z_DIMENSIONS,)))
    model.add(tf.keras.layers.BatchNormalization(momentum=0.9))
    model.add(tf.keras.layers.LeakyReLU())
    model.add(tf.keras.layers.Reshape((7,7,64)))
    model.add(tf.keras.layers.Dropout(0.4))

    model.add(tf.keras.layers.UpSampling2D())
    model.add(tf.keras.layers.Conv2DTranspose(32, kernel_size=5, padding='same', activation=None))
    model.add(tf.keras.layers.BatchNormalization(momentum=0.9))
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.UpSampling2D())
    model.add(tf.keras.layers.Conv2DTranspose(16, kernel_size=5, padding='same', activation=None))
    model.add(tf.keras.layers.BatchNormalization(momentum=0.9))
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Conv2D(1, kernel_size=5, padding='same', activation='sigmoid'))
    return model

generator = make_generator()
noise = tf.random.normal([1, Z_DIMENSIONS])
generated_image = generator(noise, training=False)

plt.imshow(generated_image[0,:,:,0], cmap='gray')

z = tf.keras.layers.Input(shape=(Z_DIMENSIONS,))
fake_image = generator(z)
discriminator.trainable = False
prediction = discriminator(fake_image)
gan_model = tf.keras.models.Model(z, prediction)
gan_model.compile(loss='binary_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.0004),
                  metrics=['accuracy']
)

def train_gan():
    for epoch in range(EPOCHS):
        # 진짜 이미지
        real_images = np.reshape(
            data[np.random.choice(data.shape[0], BATCH_SIZE, replace=False)],
            (BATCH_SIZE, 28, 28, 1)
        )

        # 가짜 이미지
        fake_images = generator.predict(np.random.uniform(-1.0,1.0,size=[BATCH_SIZE, Z_DIMENSIONS]))

        x = np.concatenate((real_images, fake_images))
        y = np.ones([2*BATCH_SIZE, 1])
        y[BATCH_SIZE:,:] = 0

        # 판별자 학습
        discriminator.trainable = True
        discriminator.train_on_batch(x, y)

        # 생성자(판별자를 속이는) 학습
        noise = np.random.uniform(-1.0, 1.0, size=[BATCH_SIZE, Z_DIMENSIONS])
        y = np.ones([BATCH_SIZE,1])
        discriminator.trainable = False
        gan_model.train_on_batch(noise, y)

        if epoch % 100 == 0:
            print(f"Epoch: {epoch}/{EPOCHS}")
            noise = np.random.uniform(-1.0, 1.0, size=[5, Z_DIMENSIONS])
            generated_images = generator.predict(noise)
            plt.figure(figsize=(10,10))
            for j in range(generated_images.shape[0]):
                plt.subplot(1,5,j+1)
                plt.imshow(generated_images[j,:,:,0], cmap='gray')
                plt.axis('off')
            plt.show()

train_gan()
