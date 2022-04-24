import tensorflow as tf
import os
import sys
import urllib.parse
import json
import cv2
import io
from PIL import Image
from math import log, exp, tan, atan, pi, ceil
import requests
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from io import StringIO

workdir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(workdir)

from scripts.get_classifier import get_classifier
from scripts.resnet_model import resnet_model
from scripts.image_helpers import sliding_window, create_legend
from scripts.coordinate_helpers import G_LatLng, getCorners, pointiterator

run = {
    "name": "resnet_model",
    "epochs": 10,
    "iterations": 1,
    "batch_size": 64,
    "learning_rate": 3e-4,
    "class_weights": False,
    "layer_sizes": [
        1024,
        512,
        128
    ],
    "dropout_factor": 0.3
}

model = get_classifier(run, resnet_model, os.path.join(workdir, 'models', 'my_model', 'my_model'))

labels = ['AnnualCrop',
          'Forest',
          'HerbaceousVegetation',
          'Highway',
          'Industrial',
          'Pasture',
          'PermanentCrop',
          'Residential',
          'River',
          'SeaLake']

color_dict = {
    0: 'orange',
    1: 'green',
    2: 'yellow',
    3: 'black',
    4: 'gray',
    5: 'brown',
    6: 'red',
    7: 'pink',
    8: 'lightblue',
    9: 'blue',
}

level_dict = {
    19: 1128.497220,
    18: 2256.994440,
    17: 4513.988880,
    16: 9027.977761,
    15: 18055.955520,
    14: 36111.911040,
    13: 72223.822090,
    12: 144447.644200,
    11: 288895.288400,
    10: 577790.576700,
    9: 1155581.153000,
    8: 2311162.307000,
    7: 4622324.614000,
    6: 9244649.227000,
    5: 18489298.450000,
    4: 36978596.910000,
    3: 73957193.820000,
    2: 147914387.600000,
    1: 295828775.300000,
    0: 591657550.500000
}

position = [47.990769, 12.004976]  # some village


def get_class_overlay_by_position(pos):
    url_params = urllib.parse.urlencode({'center': ','.join((str(pos[0]), str(pos[1]))),
                                         'zoom': 14,
                                         'size': '640x640',
                                         'maptype': 'satellite',
                                         'sensor': 'false',
                                         'scale': 1,
                                         'key': 'AIzaSyA4QuvbHhh74WAVWc_rpCJNbywBGRWL5qU'},
                                        )

    url = 'https://maps.google.com/maps/api/staticmap?' + url_params
    response = requests.get(url)
    im = Image.open(io.BytesIO(response.content))
    # im.save('pic.png')
    # x = Image.open('pic.png')
    image = im.convert("RGB")
    image = np.asarray(image, dtype=np.uint8)
    image = image[:, :, :3]

    land_usage_predictions_array = [0 for x in range(100)]
    for i, (x, y, window) in enumerate(sliding_window(image, stepSize=64, windowSize=(64, 64))):
        land_usage_predictions_array[i] = np.argmax(model.predict(window[np.newaxis, :]), axis=-1)

    return np.array(land_usage_predictions_array).flatten().reshape(10, 10)


def class_geojson_from_pos(pos, save_file=True):
    land_usage_predictions = get_class_overlay_by_position(pos)
    centerPoint = G_LatLng(pos[0], pos[1])
    edges = getCorners(centerPoint, 14, 640, 640)

    # min_lon = edges['W']
    # max_lon = edges['E']
    # min_lat = edges['N']
    # max_lat = edges['S']

    xiter = pointiterator(edges['W'], edges['E'], 10)
    yiter = pointiterator(edges['S'], edges['N'], 10)
    xx = np.fromiter(xiter, dtype=np.float)
    yy = np.flip(np.fromiter(yiter, dtype=np.float))

    geos = []
    k_new = []
    i = 0
    for i2, y in enumerate(yy[:-2]):
        for i1, x in enumerate(xx[:-1]):
            feat = {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [[xx[i1], yy[i2]],
                         [xx[i1 + 1], yy[i2]],
                         [xx[i1 + 1], yy[i2 + 1]],
                         [xx[i1], yy[i2 + 1]]]
                    ]
                },
                "properties":
                    {
                        "class": str(land_usage_predictions.ravel()[i])
                    }
            }

            geos.append(feat)
            k_new.append(land_usage_predictions.ravel()[i])
            i += 1

    geojson = {"type": "FeatureCollection",
               "features": geos
               }
    if save_file:
        with open('json_data.json', 'w') as outfile:
            json.dump(geojson, outfile)
    return geojson


# create_legend(color_dict, labels)

