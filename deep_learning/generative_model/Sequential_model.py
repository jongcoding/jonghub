from tensorflow.keras import Sequential, Model
from tensorflow.keras import layers

seq_model=Sequential()
seq_model.add(layers.Dense(4,input_shape=(10,2)))
seq_model.add(layers.Dense(4))
seq_model.add(layers.Dense(1))
seq_model.summary()