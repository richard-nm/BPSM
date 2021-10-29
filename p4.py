#!/usr/local/bin/python3

import os

for filename in os.listdir('./'):
	if filename.endswith('.dna'):
		dnafile=filename
		print('Found document {}'.format(filename))
		with open(filename) as dna:
			dna = dna.read().upper().replace(' ','').split()
			for i in dna:
				length = len(i)//100
				print("length is {0}, within range {1},{2}".format(len(i),length*100,length*100+99))	
