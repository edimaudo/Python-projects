import random, glob, sys
import os.path as osp
import tensorflow as tf
import numpy as np

from helpers_05 import grouper, flatten, fully_connected_layer
from helpers_06 import maybe_download, maybe_extract


def shuffle_arrays(*args):
    "Shuffles list of NumPy arrays in unison"
    state = np.random.get_state()
    for array in args:
        np.random.set_state(state)
        np.random.shuffle(array)


def shuffle_lists(*args):
    curr_state = random.getstate()
    for a in args:
        random.setstate(curr_state)
        random.shuffle(a)

def batches(data, labels, batch_size, shuffler=None):
    '''old batcher was array only'''
    if len(data) != len(labels):
        raise ValueError('Image data and label data must be same size')
    if batch_size > len(data):
        raise ValueError('Batch size cannot be larger than size of datasets')
    if shuffler is not None:
        assert shuffler in [shuffle_arrays, shuffle_lists]
        shuffler(data, labels)
    for res in zip(grouper(data, batch_size),
                   grouper(labels, batch_size)):
        yield res

def array_batches(*args, **kwargs):
    kwargs.setdefault('shuffler', shuffle_arrays)
    return batches(*args, **kwargs)

def list_batches(*args, **kwargs):
    kwargs.setdefault('shuffler', shuffle_lists)
    return batches(*args, **kwargs)

def download_hh(local_dir="data/hh", noisy=True):
    url = 'https://www.dropbox.com/s/c452t2dpaq8nm2y/' # hamsterhare.tar.gz?dl=1'
    fn = "hamsterhare.tar.gz"
    maybe_download(fn, url, local_dir, add_url_suffix="?dl=1", noisy=noisy)
    maybe_extract(osp.join(local_dir, fn), noisy=noisy)


def train_test_split_hh_filenames(test_pct = .2, parent_dir="data/hh"):
    hamster_dir = osp.join(parent_dir, "hamsterhare", "hamster")
    hare_dir = osp.join(parent_dir, "hamsterhare", "hare")

    jpeg = "*.JPEG"

    hamster_files = glob.glob(osp.join(hamster_dir, jpeg))
    hare_files    = glob.glob(osp.join(hare_dir, jpeg))

    all_files = list(hamster_files) + list(hare_files)
    all_labels = [0] * len(hamster_files) + [1] * len(hare_files)

    shuffle_lists(all_files, all_labels)
    train_idx = int(len(all_files) * (1.0-test_pct))

    train_files,  test_files  = all_files[ :train_idx], all_files[ train_idx:]
    train_labels, test_labels = all_labels[:train_idx], all_labels[train_idx:]
    return train_files, train_labels, test_files, test_labels

def fully_connected_xavier_relu_layer(incoming_layer, num_nodes,
                                      b_val=0.01,
                                      keep_prob=None, name=None):
    ''' from wk 05 nb: pass through for fully_connected_layer with xavier init '''
    incoming_layer = tf.convert_to_tensor(incoming_layer)
    prev_num_nodes = incoming_layer.shape.dims[-1].value

    w_stddev = np.sqrt(2.0 / prev_num_nodes)

    # from helpers_05
    return fully_connected_layer(incoming_layer, num_nodes,
                                 w_stddev = w_stddev, b_val=b_val,
                                 activation_fn = tf.nn.relu,
                                 keep_prob=keep_prob,
                                 name=name)

if __name__ == "__main__":
    download_hh()
