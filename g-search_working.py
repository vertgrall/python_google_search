# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
from __future__ import print_function
from googlesearch import search
import datetime
import os
import pickle
import sys

term = raw_input("Enter search subject: ")
count = int(raw_input("enter how many results you want: "))
extension = '.txt'
filename = raw_input("Enter a name for the file: ") + extension

lines = []
for url in search(term, stop=count):

    lines.append(url)
outfile=open(filename, 'wb')

outfile.write("\n".join(lines))
print("\n".join(lines))
