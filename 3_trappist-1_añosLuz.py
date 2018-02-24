# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:40:25 2018

@author: maquina
"""
#Recientemente se descubrieron 7 planetas similares a la Tierra y 
#potencialmente habitables que orbitan alrededor de una estrella 
#denominada TRAPPIST-1. El sistema solar se encuentra a aproximadamente 
#369 trillones de kilometros (Un trillon equivale a 1018 kilometros).
# Si asumimos que podemos viajar a la velocidad de la luz cuantos años
# luz tomaria llegar a este sistema solar.
distancia_km = 10**18
velocidad_luz_km_hora = 1.079*10**9
distancia_horas = distancia_km/velocidad_luz_km_hora
distancia_dias = distancia_horas/24
distancia_anos = distancia_dias/365.25
print(distancia_anos)