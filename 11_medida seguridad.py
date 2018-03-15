# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:49:27 2018

@author: maquina
"""

import math
s = input("Ingrese contraseña: ")
#tamaño del password
L = len(s)
#minusculas normales
#n = 27
#mayusculas y minusculas n = 52  (5.7 bits)
#n = 52
#Mayusculas, minusculas y numeros: n = 62  (5.95 bits)
#n = 62
#usando toddos los caracteres de l teclado n = 94  (6.55 bits)
n = 94

password_entropy = L * math.log2(n)

print(password_entropy)

def validadorPassword(psswrd):
    condiciones_cumplidas = 0
    #conditions_total = 3
    if len(psswrd) >= 6: 
        if psswrd.lower() != psswrd: 
        	condiciones_cumplidas += 1
        if len([x for x in psswrd if x.isdigit()]) > 0: 
        	condiciones_cumplidas += 1
        if len([x for x in psswrd if not x.isalnum()]) > 0: 
        	condiciones_cumplidas += 1
    result = False
    print (condiciones_cumplidas)
    if condiciones_cumplidas >= 2: 
    	result = True
    return result

print(validadorPassword(s))

