# we gather together some utilties and helpers from last week_04
# utilities:  shuffle, grouper, batches, get_mnist_dataset
#             show_image, test_and_show_images
# layers:     fully_connected_layer, flatten
import sys
import itertools as it
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from helpers_04 import get_mnist_dataset


def shuffle(*args):
    "Shuffles list of NumPy arrays in unison"
    state = np.random.get_state()
    for array in args:
        np.random.set_state(state)
        np.random.shuffle(array)

def grouper(iter_, n):
    """Collect data into fixed-length chunks or blocks
     grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
     from python itertools docs"""
    args = [iter(iter_)] * n
    return zip(*args)

def batches(data, labels, batch_size, randomize=True):
    if len(data) != len(labels):
        raise ValueError('Image data and label data must be same size')
    if batch_size > len(data):
        raise ValueError('Batch size cannot be larger than size of datasets')
    if randomize:
        shuffle(data, labels)
    for res in zip(grouper(data, batch_size),
                   grouper(labels, batch_size)):
        yield res

# note:
def fully_connected_layer(incoming_layer, num_nodes,
                          w_stddev=None, b_val=None,
                          activation_fn=None,
                          keep_prob=None,
                          name=None):
    ' fc layer with few defaults and default xavier init for w '
    incoming_layer = tf.convert_to_tensor(incoming_layer)
    prev_num_nodes = incoming_layer.shape.dims[-1].value

    if w_stddev is None:
        w_stddev = tf.sqrt(2.0 / prev_num_nodes)
    if b_val is None:
        b_val = 0.0 # prefer 0.01?

    with tf.name_scope(name, 'fully_connected'):
        # FIXME:  consider stddev=np.sqrt(2.0 / prev_num_nodes)
        #         [fancy initialization]
        tn = tf.truncated_normal([prev_num_nodes, num_nodes], stddev=w_stddev)
        W = tf.Variable(tn, name='W')
        const = tf.constant(b_val, shape=[num_nodes])
        b = tf.Variable(const, name='bias')

        z = tf.matmul(incoming_layer, W) + b

        # using Python's if/else expression
        # usually expect to have an activation - fallback to identity
        # we'll expect keep_prob to be None, and replace if needed
        a = activation_fn(z) if activation_fn is not None else z
        final_a = a if keep_prob is None else tf.nn.dropout(a, keep_prob)

        return final_a

def fully_connected_sigmoid_layer(incoming_layer, num_nodes,
                                  w_stddev=0.5, b_val=0.0,
                                  keep_prob=None, name=None):
    ' pass through for fully_connected_layer with simple sigmoid defaults '
    return fully_connected_layer(incoming_layer, num_nodes,
                                 w_stddev = w_stddev, b_val=b_val,
                                 activation_fn = tf.nn.sigmoid,
                                 keep_prob=keep_prob,
                                 name=name)

def fully_connected_relu_layer(incoming_layer, num_nodes,
                               w_stddev = 0.01, b_val=0.1,
                               keep_prob=None, name=None):
    ' pass through for fully_connected_layer with simple relu defaults '
    return fully_connected_layer(incoming_layer, num_nodes,
                                 w_stddev = w_stddev, b_val=b_val,
                                 activation_fn = tf.nn.relu,
                                 keep_prob=keep_prob,
                                 name=name)


def flatten(incoming, name=None):
    flat_shape = [-1, np.prod(incoming.shape[1:]).value]
    return tf.reshape(incoming, flat_shape)

def show_image(img):
    imgplot = plt.imshow(np.squeeze(img), cmap='Greys_r')

# this is a little clunky
def test_and_show_images(model, test_dict, data, labels):
    correctness, curr_preds = model.predict(test_dict)
    # setup axes
    fig, axes = plt.subplots(nrows=(len(data) // 3) + 1, ncols=3, figsize=(9,len(data)*1.5))
    axes = axes.flat
    for d, lbl, c, p, ax in zip(data, labels, correctness, curr_preds, axes):
        ax.imshow(np.squeeze(d), cmap='Greys_r') # FIXME: is cmap needed?
        ax.set_title("Predicted: {}\nCorrect: {}".format(p, bool(c)))
        ax.axis('off')
    for ax in axes: ax.set_visible(False)
