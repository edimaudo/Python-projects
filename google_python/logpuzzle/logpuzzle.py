import os
import re
import sys
import urllib
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  with open(filename) as f:
    logData = ''
    f = f.readlines()
    for data in f:
      logData+=data
    tempoutput = re.findall(r'GET (\S+)',logData)
    output = [value for value in tempoutput if value[-3:] in ['jpg','png']]
    output.sort()
    output = list(set(output))
    return output
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if os.path.exists(dest_dir):
    return "The folder already exists"
  else:
    os.mkdir(dest_dir)
    count = 0
    image_data = ""
    for url in img_urls:
      filename = "img" + str(count) + ".jpg"
      urllib.urlretrieve("https://code.google.com/" + url, filename)
      image_data += "<img src='" + filename + "'>"
      count+=1
    f = open('index.html','w')
    htmlInfo = "<html><head></head><body><p>" + image_data + "</p></body>"
    f.write(htmlInfo)
    f.close

def main():
  path = '/Users/edima/Documents/Coding/python_projects/google_python/logpuzzle' # use your own path
  log_file = ['animal_code.google.com','place_code.google.com']
  url_data = [read_urls(path + "/" + file) for file in log_file]
  
  #print(url_data)
  directory_name = 'animal_place_data'
  download_images(url_data[0], path + "/" + directory_name)

if __name__ == '__main__':
  main()
