# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:09:53 2018

@author: maquina
"""
#Se dice que dos cantidades a y b estan en proporción aurea
 #si la longitud total a+b es al segmento más largo a, como a
 #es al segmento más corto b, es decir, para a mayor que b se 
 #tiene ab=a+bb. Esta razón define una constate llamada número 
 #aureo ϕ que aparece de forma recurrente en muchos fenómenos 
# naturales. Por ejemplo, se dice que la distancia del ombligo 
# a la planta de los pies y la altura total de una persona estan
# en proporción aurea. Utilizando la observación anterior y las
# medidas experimentales de 5 compañeros encuentre una aproximación
# al número aureo ϕ.
def aureos(a, b):
    if a > b:
        uno = a/b
        dos = (a + b)/a
    return uno, dos

i = 1
prom1 = 0
prom2 = 0
while i <= 5:
    b = float(input("Altura al ombligo No." + str(i) + ": "))
    a = float(input("Altura total No." + str(i) + ": "))
    p1aureo, p2aureo = aureos(a, b)
    prom1 = prom1 + p1aureo
    prom2 = prom2 + p2aureo
    i += 1
print("Aproximación usando a/b: " + str(prom1/5))
print("Aproximación usando (a + b)/a: " + str(prom2/5))