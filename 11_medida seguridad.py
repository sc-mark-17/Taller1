# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:49:27 2018

@author: maquina
"""

import math
s = input("Ingrese contraseña: ")
#length of the password
L = len(s)
#pool size of characters
#n = 27
#Upper and lower case gives you n = 52  (5.7 bits)
#n = 52
#Upper and lower case, and numbers: n = 62  (5.95 bits)
#n = 62
#Using all keyboard characters: n = 94  (6.55 bits)
n = 94

password_entropy = L * math.log2(n)

print(password_entropy)

def validate_password(passwd):
    conditions_met = 0
    #conditions_total = 3
    if len(passwd) >= 6: 
        if passwd.lower() != passwd: conditions_met += 1
        if len([x for x in passwd if x.isdigit()]) > 0: conditions_met += 1
        if len([x for x in passwd if not x.isalnum()]) > 0: conditions_met += 1
    result = False
    print (conditions_met)
    if conditions_met >= 2: result = True
    return result

print(validate_password(s))

