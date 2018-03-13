# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:58:39 2018

@author: maquina
"""

#Escriba un programa que verifique si un punto se 
#encuentra en un circulo de radio 1 con centro en 10,10
import math
x = int(input("Digite la coordenada \"x\" del punto: "))
y = int(input("Digite la coordenada \"y\" del punto: "))
cx, cy = 10, 10
x = x - cx
y = y - cy
def pitagoras(x,y):
    total = x**2 + y**2
    h = math.sqrt(total)
    return h

if pitagoras(x,y) <= 1:
    print("El punto SI esta dentro del circulo")
else:
    print("El punto NO esta dentro del circulo")