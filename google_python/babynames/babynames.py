
import sys
import re
from os import listdir
from os.path import isfile, join
from operator import itemgetter
"""Baby Names exercise

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  wordData = ""
  with open(filename, 'r') as txtfile:
    for row in txtfile:
      for word in row:
        wordData+=word
  
  year_search = "Popularity in "
  year_position = wordData.find(year_search) 
  year = wordData[year_position + len(year_search):year_position + len(year_search) + 4]

  userInfo = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', wordData)
  sorted_a = sorted(userInfo,key=itemgetter(1))
  output = []
  output.append(year)
  for info in sorted_a:
    output.append(info[1] + " " + info[0])
  return output



def main():
  mypath = '/Users/edima/Desktop/google-python-exercises/babynames/babydata' #use your own path
  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  fileData = [file for file in onlyfiles if file[0:4]=='baby']

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for file in fileData:
    print(extract_names(mypath + "/" + file))
  #print(extract_names(mypath + "/" + 'baby1990.html'))

if __name__ == '__main__':
  main()
