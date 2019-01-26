import os.path as osp
import os
import requests

def urlretrieve(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
    return path, r.headers

def mkdir(path):
    if not osp.exists(path):
        os.makedirs(path)

def download(url, _dir):
    if not osp.exists(_dir):
        mkdir(_dir)

    filename = url.rsplit('/',1)[1]
    fullpath = osp.join(_dir, filename)
    if not osp.exists(fullpath):
        urlretrieve(url, fullpath)
    return fullpath

def test_download():
    data_dir = 'tst_data'
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.{}'
    download(url.format('data'), data_dir)
    download(url.format('names'), data_dir)

if __name__ == "__main__":
    test_download()
