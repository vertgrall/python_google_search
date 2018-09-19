# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
from __future__ import print_function
from googlesearch import search
import datetime
import os
import pickle
import sys

term = raw_input("Enter search subject: ")
lines = []
for url in search(term, stop=20):
#for url in search('"Seattle" Makers', stop=20):
    lines.append(url)
outfile=open('./searchresults.txt', 'wb')
# updated area
outfile.write("\n".join(lines))
print("\n".join(lines))