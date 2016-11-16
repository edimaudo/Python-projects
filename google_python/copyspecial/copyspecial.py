import sys
import re
import os
import shutil
import commands
from os import listdir
from os.path import isfile, join

"""Copy Special exercise
"""

def get_special_paths(dir):
  output = []
  for f in listdir(dir):
    if isfile(join(dir,f)):
      output.append(os.path.dirname(dir) + "/" + f)
  return output

def copy_to(paths, dir):
  if os.path.exists(paths) and os.path.exists(dir):
    shutil.copy(dir, paths)
  return

def zip_to(paths, zippath):
  return



def main():
  # +++your code here+++
  # Call your functions
  frompath = '/Users/edima/Desktop/google-python-exercises/copyspecial' # use own path
  topath = '/Users/edima/Desktop/google-python-exercises/copyspecial/copyLocation' # use own path

  #print(get_special_paths(frompath))
  def copy_to(topath, frompath)

if __name__ == "__main__":
  main()
