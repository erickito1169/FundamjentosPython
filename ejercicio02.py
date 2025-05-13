################################################################################
#Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################

print("programa que calcula area y perimetro de un Rectangulo")

altura = input ("Ingresa la altura: ")
altura = int(altura)
base = int(input ("ingresa la base: "))

perimetro = base + altura + base + altura
area = base * altura 

print ("el area del rectangulo es: " + str(area))
print ("el perimetro des rectangulo es: "+ str(perimetro))
