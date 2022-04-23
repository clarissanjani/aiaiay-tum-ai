import tensorflow as tf
import os
import sys

workdir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(workdir)
# from scripts.resnet_model import resnet_model


def get_classifier(run, model, weights_path):
    model = model(run)
    model.load_weights(weights_path)
    return model
