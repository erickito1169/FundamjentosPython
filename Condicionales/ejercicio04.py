# //################################################################################
# // Crea un programa que pida al usuario dos números y muestre su división 
# //si el segundo no es cero, o un mensaje de aviso en caso contrario.
# //################################################################################

numero1 = int(input("ingresa un numero: "))
numero2 = int(input("ingresa otro numero: "))

if numero2 !=0:
    division = numero1 / numero2
    print("el resultado es", division)
else:
    print ("el segumdo numero no debe ser cero")