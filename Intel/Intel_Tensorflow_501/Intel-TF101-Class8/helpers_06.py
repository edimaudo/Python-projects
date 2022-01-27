import os, tarfile, sys, random
import os.path as osp
import itertools as it
import numpy as np
import tensorflow as tf

from helpers_02 import urlretrieve
from helpers_04 import mkdir
from helpers_05 import flatten


def maybe_download(filename, url, directory,
                   force=False, noisy=True, add_url_suffix=""):
    """Download a file if not present."""
    mkdir(directory)

    joined = osp.join(directory, filename)
    if force or not osp.exists(joined):
        urlretrieve(url + filename + add_url_suffix, joined)
        if noisy:
            print('Download complete for {}'.format(filename))
        return joined
    else:
        if noisy:
            print('File {} already present.'.format(filename))
    return joined

def maybe_extract(filename, force=False, noisy=True):
    root = osp.splitext(osp.splitext(filename)[0])[0]  # remove .tar.gz
    if osp.isdir(root) and not force:
        # You may override by setting force=True.
        if noisy:
            print('File {} already present from {}.'.format(root, filename))
    else:
        if noisy:
            print('Extracting data for {}.'.format(root))
        tar = tarfile.open(filename)
        sys.stdout.flush()
        tar.extractall(root[0:root.rfind('/') + 1])
        tar.close()
    return root

def fetch_alexnet_weights_and_classes():
    directory = 'data/alexnet/'
    url = 'http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/'
    remote_weights_file = 'bvlc_alexnet.npy'
    remote_labels_file = 'caffe_classes.py'

    local_weights_file = maybe_download(remote_weights_file, url, directory)
    local_labels_file = maybe_download(remote_labels_file, url, directory)

    weights = np.load(local_weights_file, encoding='bytes').item()

    # ugly:  but that's how guerzhoy provides the names
    #        defines the variable class_names
    from data.alexnet.caffe_classes import class_names

    return weights, class_names




if __name__ == "__main__":
    fetch_alexnet_weights_and_classes()
