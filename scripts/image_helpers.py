import numpy as np
import matplotlib.pyplot as plt


def sliding_window(image, stepSize, windowSize):
    # slide a window across the image
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            # yield the current window
            yield x, y, image[y:y + windowSize[1], x:x + windowSize[0]]


def export_legend(legend, filename="legend.png", expand=None):
    if expand is None:
        expand = [-2, -2, 2, 2]
    fig = legend.figure
    fig.canvas.draw()
    bbox = legend.get_window_extent()
    bbox = bbox.from_extents(*(bbox.extents + np.array(expand)))
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)


def create_legend(color_dict, labels):
    f = lambda m, c: plt.plot([], [], marker=m, color=c, ls="none")[0]
    handles = [f("s", color_dict[i]) for i in range(10)]
    legend = plt.legend(handles, labels, loc=3, framealpha=1, frameon=True)
    export_legend(legend)
