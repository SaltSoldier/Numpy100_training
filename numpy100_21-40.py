# -*- coding: utf-8 -*-
"""
numpy100_training 21~40

Created on Thu Jun  9 21:50:41 2016

@author: B5_2
"""
import numpy as np

#
print("No.21 ")
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
print("\n")

#
print("No.22 ")
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print("\n")

#
print("No.23 ")
Z = np.zeros((5,5))
Z += np.arange
print(Z)
print("\n")

#
print("No.24 ")
def generate():
    for x in xrange(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
print("\n")
