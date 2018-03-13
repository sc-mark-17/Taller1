# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:08:56 2018

@author: maquina
"""
import math

def bsa(w,h):
    a = math.sqrt((w*h)/3600)
    return a

w = float(input("Peso (kg): "))
h = float(input("Altura (cm): "))

print("BSA = " + str(bsa(w,h)) + " metros cuadrados")