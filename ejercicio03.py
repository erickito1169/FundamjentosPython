################################################################################
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
################################################################################

#hipotenusa ** 2 =cateto1 ** 2 + cateto2 ** 2

cateto1 = int(input("ingresa valor de cateto 1: "))
cateto2 = int(input("ingresa valor de cateto 2: "))

import math
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print ("La hipoenusa del triangulo es: "+ str(hipotenusa))