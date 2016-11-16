import sys
import re
import os
import shutil
import commands
from os import listdir
from os.path import isfile, join
import zipfile

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
  if os.path.exists(zippath):
    return "No file to zip to "
  else:
    output = get_special_paths(paths)
    for value in output:
      shutil.make_archive(output_filename, 'zip', zippath)
    return "Done"




def main():
  # +++your code here+++
  # Call your functions
  frompath = '/Users/edima/Desktop/google-python-exercises/copyspecial' # use own path
  topath = '/Users/edima/Desktop/google-python-exercises/copyspecial/copyLocation' # use own path

  #print(get_special_paths(frompath))
  #copy_to(topath, frompath)
  #zip_to(frompath,topath)

if __name__ == "__main__":
  main()
