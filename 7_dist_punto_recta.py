# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 00:27:06 2018

@author: maquina
"""

#Escriba un programa que calcule la distancia m ́as corta de un punto a una
#lınea.
import math
x = int(input("x: "))
y = int(input("y: "))

lx1 = int(input("Linea x1: "))
ly1 = int(input("Linea y1: "))
lx2 = int(input("Linea x2: "))
ly2 = int(input("Linea y2: "))

m = (ly2 - ly1)/(lx2 - lx1)
b = ly1 - m * lx1
dist = (m * x - y + b)/math.sqrt((m**2) + 1)
print(dist)