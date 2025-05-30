#//################################################################################
#//Escribir por pantalla cada carácter de una cadena introducida por teclado.
#//################################################################################

mi_string = input("ingresa un texto: ")

print(mi_string)

for letra in mi_string:
    print(letra, end=" - ")

print()

# La funcion nos da el tamaño de un string 
for index in range(len(mi_string)):
    print(f"[{index}] = {mi_string[index] }")

other_string = "prueba"

print(other_string[0])
print(other_string[3])
print(other_string[5])