import tensorflow as tf
import numpy as np
import sys, zipfile

import os.path as osp

from helpers_04 import mkdir
from helpers_06 import maybe_download

# originally from wk 05 helpers
def flatten(incoming, name=None):
    flat_shape = [-1, np.prod(incoming.shape[1:]).value]
    return tf.reshape(incoming, flat_shape)

# updated from wk 05 helpers variable_scope/get_variable
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

    with tf.variable_scope(name, 'fully_connected'): #, reuse=True):
        with tf.device('/cpu:0'): # force params on cpu
            tn = tf.truncated_normal_initializer(stddev=w_stddev)
            W = tf.get_variable('W', shape=[prev_num_nodes, num_nodes], initializer=tn)
            const = tf.constant_initializer(b_val)
            b = tf.get_variable(name='bias', shape=[num_nodes], initializer=const)

        # these can be placed on GPU if TF wants to
        z = tf.matmul(incoming_layer, W) + b
        a = activation_fn(z) if activation_fn is not None else z
        final_a = a if keep_prob is None else tf.nn.dropout(a, keep_prob)

        return final_a


# originally from week 07 nb
# (note, now uses the updated var_scope/get_var above)
def fully_connected_xavier_relu_layer(incoming_layer, num_nodes,
                                      b_val=0.01,
                                      keep_prob=None, name=None):
    ''' pass through for fully_connected_layer with xavier init '''
    incoming_layer = tf.convert_to_tensor(incoming_layer)
    prev_num_nodes = incoming_layer.shape.dims[-1].value

    w_stddev = np.sqrt(2.0 / prev_num_nodes)

    return fully_connected_layer(incoming_layer, num_nodes,
                                 w_stddev = w_stddev, b_val=b_val,
                                 activation_fn = tf.nn.relu,
                                 keep_prob=keep_prob,
                                 name=name)

# updated from week 5 nb with variable_scope/get_variable
def conv_layer(incoming, num_kernels, kernel_sz,
               strides=[1, 1, 1, 1], padding='SAME',
               b_val=0.01,
               activation_fn=tf.nn.relu,
               name=None):
    prev_outshape = incoming.shape.dims[-1].value
    kshape = kernel_sz + [prev_outshape, num_kernels]

    fan_in = np.prod(incoming.shape[1:]).value
    xavier_stddev = np.sqrt(2.0 / fan_in)

    with tf.variable_scope(name, 'conv_layer'): # , reuse=True):
        with tf.device('/cpu:0'): # force params on cpu
            tn = tf.truncated_normal_initializer(stddev=xavier_stddev)
            w = tf.get_variable(name='kernel', shape=kshape, initializer=tn)
            const = tf.constant_initializer(b_val)
            b = tf.get_variable(name='bias', shape=[num_kernels], initializer=const)
        # these can be placed on GPU
        conv = tf.nn.conv2d(incoming, w, strides, padding, name='conv')
        z = tf.nn.bias_add(conv, b)
        return z if activation_fn is None else activation_fn(z)


# originally from week 5 nb
def pool_layer(incoming, ksize, strides=None, padding='VALID',
               pool_fn=tf.nn.max_pool, name=None):
    'create a pooling layer:  we auto-add the leading/trailing 1s'
    ksize = [1] + ksize + [1]
    # default strides to ksize
    strides = strides if strides is not None else ksize
    with tf.name_scope(name, 'pool_layer'):
        return pool_fn(incoming, ksize, strides, padding)


def grab_tin():
    ' grab the tiny imagenet dataset and return the path to its root '
    filename = "tiny-imagenet-200.zip"
    base_url = 'http://cs231n.stanford.edu/'
    directory = "data"

    expanded_data_path = osp.join(directory, 'tin')
    if osp.exists(expanded_data_path):
        return expanded_data_path

    zip_path = maybe_download(filename, base_url, directory)


    zipped = zipfile.ZipFile(zip_path, 'r')
    zipped.extractall(expanded_data_path)
    zipped.close()

    return expanded_data_path

def get_tin_id_maps(path):
    full_path = osp.join(path, 'tiny-imagenet-200', 'wnids.txt')
    id_to_synset = [line.rstrip() for line in open(full_path)]
    synset_to_id = dict((s,idx) for idx,s in enumerate(id_to_synset))
    return id_to_synset, synset_to_id

if __name__ == "__main__":
    # print(grab_tin())
    print(get_tin_id_maps("data/tin"))
