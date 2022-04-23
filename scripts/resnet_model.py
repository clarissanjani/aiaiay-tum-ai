from tensorflow.keras import layers
import tensorflow as tf


def resnet_model(run, img_input_shape=(64, 64, 3), n_labels=10):
    inputs = layers.Input(shape=img_input_shape)
    resnet = tf.keras.applications.resnet50.ResNet50(
        include_top=False, weights='imagenet', input_tensor=inputs,
        input_shape=img_input_shape, pooling='avg')
    for i in resnet.layers:
        i.trainable = False
    x = resnet(inputs)
    x = layers.Dense(run['layer_sizes'][0], activation='relu')(x)
    x = layers.Dropout(run['dropout_factor'])(x)
    x = layers.Dense(run['layer_sizes'][1], activation='relu')(x)
    x = layers.Dropout(run['dropout_factor'])(x)
    x = layers.Dense(run['layer_sizes'][2], activation='relu')(x)
    x = layers.Dropout(run['dropout_factor'])(x)

    output = tf.keras.layers.Dense(n_labels, activation='sigmoid', name='output')(x)
    model = tf.keras.Model(inputs=[inputs], outputs=[output])

    print(model.summary())
    return model
