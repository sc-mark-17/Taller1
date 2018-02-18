# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:09:53 2018

@author: maquina
"""
#Escriba un programa que calcule el volumén de una esfera dado su radio.

import math
r = int(input("Digite el radio de la esfera: "))
v = (3/4) * (math.pi) * (r**3)
print("El volumén de la esfera es: " + str(v))