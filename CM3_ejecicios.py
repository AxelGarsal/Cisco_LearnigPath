# Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.

for i in range(11):
    if i % 2 != 0:
        print(i, end=" ")

#Ejercicio 2

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
print("")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 != 0:
        print(numero, end=' ')


# Ejercicio 3

# Crea un programa con un bucle for y una declaración break.
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.

correo = input('\n Dame tu correo: ')
for i in correo:
    if i == '@':
        break
    print(i, end='')

# Ejercicio 4

# Crea un programa con un bucle for y una declaración continue.
# El programa debe iterar sobre una cadena de dígitos,
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
print('')
for digito in "016503180651093010200870":
    if digito == '0':
        print('x', end='')
        continue
    print(digito, end='')
