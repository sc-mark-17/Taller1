# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 00:53:05 2018

@author: maquina
"""
import math

class circulo:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def distancia(c1, c2):
    d = math.sqrt(((c2.x - c1.x)**2) + ((c2.y - c1.y)**2))
    return d

if __name__=="__main__":
    print("Coordenadas centro de los circulos y su radio correspondiente: ")
    print("Circulo 1: ")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    r1 = float(input("r: "))
    c1 = circulo(x1, y1, r1)
    print("Circulo 2: ")
    x2 = int(input("x: "))
    y2 = int(input("y: "))
    r2 = float(input("r: "))
    c2 = circulo(x2, y2, r2)
    d = distancia(c1, c2)
    if d > (c1.r + c2.r):
        print("No se intersectan")
    else:
        print("Si se intersectan")
