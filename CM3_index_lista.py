# Escribir una línea de código que solicite al usuario que reemplace el número central en la lista
# con un número entero ingresado por el usuario (paso 1).
# Escribir una línea de código que elimine el último elemento de la lista (paso 2).
# Escribir una línea de código que imprima la longitud de la lista existente (paso 3).

numeros = [13, 9, 2021, 8, 23]
print(numeros)
nuevo = int(input('Dame el nuevo número: '))
numeros[2]=nuevo
print(numeros)
del numeros[-1]
print(numeros)
print(len(numeros))
