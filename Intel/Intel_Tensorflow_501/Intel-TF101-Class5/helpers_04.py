import numpy as np
import os, tarfile, gzip, sys, pickle
import os.path as osp
from six.moves.urllib.request import urlopen

from helpers_02 import urlretrieve

def mkdir(path):
    if not osp.exists(path):
        os.makedirs(path)
    return path

def download(url, path):
    if not os.path.exists(path):
        urlretrieve(url, path)
    return path


def _read32(bytestream):
    # Data type is big-endian, 32-bit unsigned integer
    dtype = np.dtype(np.uint32).newbyteorder('>')
    return np.frombuffer(bytestream.read(4), dtype=dtype)[0]

def mnist_load_images(filename):
    with open(filename, 'rb') as f:
        with gzip.GzipFile(fileobj=f) as bytestream:
            magic = _read32(bytestream)
            if magic != 2051:
                raise ValueError("Encountered invalid magic number {} in image file {}".format(magic, f.name))
            num_images = _read32(bytestream)
            rows = _read32(bytestream)
            cols = _read32(bytestream)
            buffer = bytestream.read(num_images * rows * cols)
            data = np.frombuffer(buffer, dtype=np.uint8)
            data = np.float32(data.reshape(num_images, rows, cols, 1))
            return data


def mnist_load_labels(filename):
    with open(filename, 'rb') as f:
        with gzip.GzipFile(fileobj=f) as bytestream:
            magic = _read32(bytestream)
            if magic != 2049:
                raise ValueError("Encountered invalid magic number {} in label file {}".format(magic, f.name))
            num_labels = _read32(bytestream)
            buffer = bytestream.read(num_labels)
            labels = np.int32(np.frombuffer(buffer, dtype=np.uint8))
            return labels


def create_mnist_dataset(save_numpy=True):
    mkdir('data')
    train_data_url   = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
    train_labels_url = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
    test_data_url    = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
    test_labels_url  = 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'

    is_down = False

    try:
        urlopen('http://yann.lecun.com/', timeout=5)
    except IOError:
        print('http://yann.lecun.com/ is down. Using internet archive as alternative.')
        is_down = True

    if is_down:
        archive_prefix = 'https://web.archive.org/web/20160828233817/'
        train_data_url   = archive_prefix + train_data_url
        train_labels_url = archive_prefix + train_labels_url
        test_data_url    = archive_prefix + test_data_url
        test_labels_url  = archive_prefix + test_labels_url

    train_data_path   = download(train_data_url,   'data/mnist-train-images.gz')
    train_labels_path = download(train_labels_url, 'data/mnist-train-labels.gz')
    test_data_path    = download(test_data_url,    'data/mnist-test-images.gz')
    test_labels_path  = download(test_labels_url,  'data/mnist-test-labels.gz')

    train_data   = mnist_load_images('data/mnist-train-images.gz')
    train_labels = mnist_load_labels('data/mnist-train-labels.gz')
    test_data    = mnist_load_images('data/mnist-test-images.gz')
    test_labels  = mnist_load_labels('data/mnist-test-labels.gz')

    if save_numpy:
        np.save('data/mnist-train-images.npy', train_data)
        np.save('data/mnist-train-labels.npy', train_labels)
        np.save('data/mnist-test-images.npy',  test_data)
        np.save('data/mnist-test-labels.npy',  test_labels)

    return train_data, train_labels, test_data, test_labels


def get_mnist_dataset():
    mnist_numpy_paths = {'train_data'  : 'data/mnist-train-images.npy',
                         'train_labels': 'data/mnist-train-labels.npy',
                         'test_data'   : 'data/mnist-test-images.npy',
                         'test_labels' : 'data/mnist-test-labels.npy'}

    for key, path in mnist_numpy_paths.items():
        if not osp.exists(path):
            return create_mnist_dataset(True)

    train_data   = np.load(mnist_numpy_paths['train_data'])
    train_labels = np.load(mnist_numpy_paths['train_labels'])
    test_data    = np.load(mnist_numpy_paths['test_data'])
    test_labels  = np.load(mnist_numpy_paths['test_labels'])

    return train_data, train_labels, test_data, test_labels


def extract_tar(filename, force=False):
    root = os.path.splitext(os.path.splitext(filename)[0])[0]  # remove .tar.gz
    if os.path.isdir(root) and not force:
        # You may override by setting force=True.
        print('{} already present - don\'t need to extract {}.'.format(root, filename))
    else:
        print('Extracting data for {}. This may take a while. Please wait.'.format(root))
        tar = tarfile.open(filename)
        sys.stdout.flush()
        tar.extractall(root[0:root.rfind('/') + 1])
        tar.close()
    return root

def cifar_unpickle(file):
    fo = open(file, 'rb')
    data = pickle.load(fo, encoding='latin1')
    fo.close()
    return data

def download_cifar():
    mkdir('data/cifar')
    path = download('https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',
                    osp.join('data/cifar', 'cifar-10-python.tar.gz'))
    extract_tar(path)
    data_dir = osp.join('data/cifar', 'cifar-10-batches-py')

    train_data = []
    train_labels = []
    for i in range(1,6):
        batch_path = osp.join(data_dir, 'data_batch_{}'.format(i))
        data_dict = cifar_unpickle(batch_path)
        train_data.append(data_dict['data'])
        train_labels.append(data_dict['labels'])
    train_data = np.concatenate(train_data)
    train_labels = np.concatenate(train_labels).astype(np.int32)

    # Load test data and labels
    test_path   = osp.join(data_dir, 'test_batch')
    test_dict   = cifar_unpickle(test_path)
    test_data   = test_dict['data']
    test_labels = np.array(test_dict['labels'], dtype=np.int32)

    data_dir = "data/cifar"
    np.save(osp.join(data_dir,'cifar-train-images.npy'), train_data)
    np.save(osp.join(data_dir,'cifar-train-labels.npy'), train_labels)
    np.save(osp.join(data_dir,'cifar-test-images.npy'), test_data)
    np.save(osp.join(data_dir,'cifar-test-labels.npy'), test_labels)

def load_cifar():
    if not osp.exists('data/cifar/cifar-test-labels.npy'):
        print("attempting to download cifar")
        download_cifar()

    data_dir = "data/cifar"
    train_data   = np.load(osp.join(data_dir, 'cifar-train-images.npy'))
    train_labels = np.load(osp.join(data_dir, 'cifar-train-labels.npy'))
    test_data    = np.load(osp.join(data_dir, 'cifar-test-images.npy'))
    test_labels  = np.load(osp.join(data_dir, 'cifar-test-labels.npy'))

    ids_path = os.path.join(data_dir,
                            'cifar-10-batches-py', 'batches.meta')
    readable_labels = cifar_unpickle(ids_path)['label_names']

    return (train_data, train_labels,
            test_data, test_labels), readable_labels

if __name__ == "__main__":
    # get_mnist_dataset()
    load_cifar()
