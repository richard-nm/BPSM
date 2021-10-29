#!/usr/local/bin/python3
import os

with open('aj.fasta') as aj:
	aj=aj.read().upper().replace(' ','').replace('\n','')
	count = 0
	for i in range(0,len(aj)-30,3):
		count += 1
		content=aj[i:i+30]
		g=content.count('G')
		c=content.count('C')
		print(">AJ223353_coding_{0}_{1}_window30_offset3".format(count,content))	
		print(content, end="\t")
		print(round((g+c)/30,2))
		
