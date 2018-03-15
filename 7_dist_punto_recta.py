# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 00:27:06 2018

@author: maquina
"""

#Escriba un programa que calcule la distancia m ́as corta de un punto a una
#lınea.
import math
x = 4
y = 4

A = 1
B = 2
C = -4

d = (abs((A*x) + (B*y) + (C)))/(math.sqrt((A**2) + (B**2)))
print(d)