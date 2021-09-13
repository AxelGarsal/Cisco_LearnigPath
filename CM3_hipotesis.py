# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante
# (aún no se ha comprobado) que se puede describir de la siguiente manera:

# Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
# Si es par, evalúa un nuevo c0 como c0 ÷ 2.
# De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
# Si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.


numero = int(input('Ingresa un numero para probar la hipoteis: '))
pasos = 0
while numero > 0 and numero != 1:
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero = (numero * 3) + 1
    pasos = pasos + 1
    print(numero)
print("La cantidad de pasos para evaluar tu hipotesis son:", pasos)
