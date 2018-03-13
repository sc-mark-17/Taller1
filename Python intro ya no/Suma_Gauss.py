# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 07:33:43 2018

@author: maquina
"""
def sumGauss(n):
    g = (n*(n + 1))/2
    return g
g = int(input("¿De cuantos números quiere saber su suma gausseana? "))
a = sumGauss(g)
print("La suma gausseana es: " + str(int(a)))