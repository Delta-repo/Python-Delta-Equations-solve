import os
import math

print('Calculer les fonctions du premier degré:')

a = float(input("A (0x2) = "))
b = float(input("B (0x)= "))
c = float(input("C (0)= "))

clear = lambda: os.system('cls')
clear()


print('Pour trouver Delta : ',b,'2 - 4.',a,'.',c)
d = b**2 - 4*a*c

print('Delta est égale à : ' ,d,)

if(d < 0):
    print("L'équation n'a pas de solution :") 
else:
    if (d == 0):
        print("L'équation a une solution double :")
        x = -b / (2.*a)
        print ("La solution est x = ",x)
    else:
        print("L'équation a deux solutions solutions :")
        x1 = (-b - math.sqrt(d)) /(2*a)
        x2 = (-b + math.sqrt(d)) /(2*a)
        print ("x1 = ",x1)
        print ("x2 = ",x2)
