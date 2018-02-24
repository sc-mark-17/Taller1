# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:54:07 2018

@author: maquina
"""
#Escriba un programa que calcule la suma de 12+22+32...+n2


n = int(input("Digite n: "))

#Algoritmo 1
i = 1
cont = 0
while i <= n:
    cont += i**2
    i += 1
    
print (cont)

#Algoritmo 2
a = ((n)*(n + 1)*((2*n) + 1))/6

print(a)