#!/usr/local/bin/python3
import os

with open("genomic_dna2.txt") as dna:
	dna = dna.read().upper()
	with open("exons.txt") as ex:
		ex = ex.read().replace(",","\n").split()
		with open('t2.txt','w') as t:
			for i in range(0,len(ex),2):
				t.write(dna[int(ex[i]):int(ex[i+1])])
			
