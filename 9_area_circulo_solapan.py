# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:25:15 2018

@author: maquina
"""

#Escriba un programa que calcule el  ́area de dos c ́ırculos que se solapan.
import math
def interseccionArea(x0, y0, r0, x1, y1, r1):
  R0 = r0 * r0
  R1 = r1 * r1
  distan = math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))

  #circulos que no se solapan
  if (distan > r1 + r0):
      return 0
  # circulo 1 esta completamente dentro del circulo 2
  elif (distan <= abs(r0 - r1) and r0 >= r1):
      #area del circulo 1
      return math.PI * R1
  #circulo 0 completamente dentro del circulo 1
  elif (distan <= abs(r0 - r1) and r0 < r1):
      #area circulo 0
      return math.PI * R0
  #circulo solapado parcialmente
  else:
      phi = (math.acos((R0 + (distan * distan) - R1) / (2 * r0 * distan))) * 2
      theta = (math.acos((R1 + (distan * distan) - R0) / (2 * r1 * distan))) * 2
      area1 = 0.5 * theta * R1 - 0.5 * R1 * math.sin(theta)
      area2 = 0.5 * phi * R0 - 0.5 * R0 * math.sin(phi)
      #area interseccion
      return area1 + area2
if __name__ == '__main__':
    area = interseccionArea(0,0,3,3,0,3)
    print(area)
