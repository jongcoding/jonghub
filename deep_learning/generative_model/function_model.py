from tensorflow.keras import Sequential, Model, Input
from tensorflow.keras import layers

input1 = Input(shape=(10,2))
lay1 = layers.Dense(4, input_shape=(10,2))(input1)
lay2 = layers.Dense(4)(lay1)
out1 = layers.Dense(1)(lay2)
out2 = layers.Dense(1)(lay2)
func_model = Model(inputs=input1, outputs=[out1, out2])
