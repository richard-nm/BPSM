#!/usr/local/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import os

def ecoli():
  with open("ecoli.txt") as eco:
    eco= eco.read().replace('\n','').upper()[0:100000]
  at=[]
  window=1000
  for i in range(len(eco)-window):
    win = eco[i:i+window]
    at.append(win.count('AT')/window)
  plt.figure(figsize=(20,10))
  plt.plot(at,label='AT',linewidth=3)
  plt.legend()
  plt.xlabel('fob')
  # plt.text(40000,0.1,r'$\mu=1$')
  plt.ylabel('position')
  plt.savefig('1.png')
  plt.show()


def align():
  with open("alignment.txt") as alg:
    alg.read().upper().split('\n')
  
ecoli()
