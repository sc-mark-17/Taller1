# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:21:51 2018

@author: maquina
@creditos: http://python-esp.blogspot.com.co/2010/01/calculo-del-punto-de-interseccion-de-2.html?m=1
"""

#Escriba un programa que verifique si dos
#segmentos de línea recta se intersectan

#!/usr/bin/python
# coding=utf-8
#Calcula el punto de intersección de 2 líneas
class punto:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+")"
class linea:
  def __init__(self, p0, p1):
    self.p0 = p0
    self.p1 = p1
    self.A = p1.x - p0.x
    self.B = p1.y - p0.y
    self.C = p1.x*p0.y - p0.x*p1.y
  def intersecta(self, otro):
    det = self.A*otro.B - otro.A*self.B
    print("Det:" + str(det))
    x = otro.A*self.C-self.A*otro.C
    print("x:" + str(x))
    y = otro.B*self.C-self.B*otro.C
    print("y:" + str(y))
    return punto(x/det,y/det)
   
  def __str__(self):
      s = ("P0:" + str(self.p0) + ", P1:" + str(self.p1) + "\n" + 
           "A:" + str(self.A) + " B:" + str(self.B) + " C:" + str(self.C) + "\n\n")
      return s 
   
if __name__=="__main__":
  L1 =linea(punto(5,1),punto(10,10))
  L2 =linea(punto(12,0),punto(1,13)) 
  print (L1,L2)
  print ("Punto de intersección:"+str(L1.intersecta(L2)))