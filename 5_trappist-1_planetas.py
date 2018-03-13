# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:53:05 2018

@author: maquina
"""

#De todos los planetas que orbitan alrededor de TRAPPIST-1
#cual es el planeta que de acuerdo a su temperatura usted podría 
#habitar más facilmente

#temperatura promedio de la tierra en el 2017 en grados Celsius
tierra = 14.75

#temperatura de los planetas de TRAPPIST-1 en kelvin
tempTrappist_1_kelvin = dict(b=400, c=342, d=288, e=251, f=219, g=199, h=167)
tierraKelvin = tierra + 273
comparacionTemp = {}
minimo = 1000
for k, v in tempTrappist_1_kelvin.items():
    comparacionTemp[k] = abs(tierraKelvin - v)
    if minimo > abs(tierraKelvin - v):
        minimo = abs(tierraKelvin - v)
        keyy = k

print("El planeta más fácilmente habitable es el " + str(keyy))


    