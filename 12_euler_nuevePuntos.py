# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:52:21 2018

@author: maquina
"""

#Dado un triángulo determine la ecuación 
#de recta de Euler y la circunferencia de los nueve puntos**.

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pedirDatosABC():
    print("Digite los puntos del triángulo ABC:")
    print("A: ")
    x = input("Ax: ")
    y = input("Ay: ")
    A = punto( x, y)
    print("B: ")
    x = input("Bx: ")
    y = input("By: ")
    B = punto( x, y)
    print("C: ")
    x = input("Cx: ")
    y = input("Cy: ")
    C = punto( x, y)
    


if __name__ == "__main__":
    pedirDatosABC()
    