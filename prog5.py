import sys
import os
from functools import reduce


dict = {}
wordlen = []

if (len(sys.argv) != 2):
	print "invalid arguments"
	sys.exit()

if (not(os.path.exists(sys.argv[0]))):
	print "invalid file path"
	sys.exit()

if (sys.argv[1].split('.')[-1] != "txt"):
	print " invalid file format, only txt is allowed "
	sys.exit()

with open(sys.argv[1]) as file:
	for line in file: 
		for word in line.split():
			dict[word] = dict.get(word,0) + 1 
print dict




