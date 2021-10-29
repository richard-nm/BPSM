#!/usr/local/bin/python3

import os

with open("input.txt") as file:
	filec = file.read().split()
	with open("cleanup","w")as clean:
		for i in filec:
			for m in i[14:]:
				clean.write(m)
			clean.write('\n')
			print(i[14:])
			print(len(i[14:]))
