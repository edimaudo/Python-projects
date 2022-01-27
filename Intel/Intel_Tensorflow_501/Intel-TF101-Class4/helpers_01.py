import os.path as osp
import itertools

def get_fresh_dir(parent_dir):
    ''' get an unused directory name in parent_dir '''
    import itertools as it
    import os.path as osp
    for i in it.count():
        possible_dir = osp.join(parent_dir, str(i))
        if not osp.exists(possible_dir):
            return possible_dir
