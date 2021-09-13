# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores,
# y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas:
# si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa,
# terminan su trabajo inmediatamente.

#bloques = int(input('Ingresa tu cantidad de bloques: '))
#pisos = 0
#j = 0
#while bloques - (bloques - j) >= 0:
#    for i in range(1, bloques, 1):
#        bloques = bloques - i
#        pisos = pisos + 1
#        if bloques < 0:
#            continue
#        print(pisos)


# bloques = int(input('Ingresa tu cantidad de bloques: '))
# pisos = 0
# while bloques > 1:
#    for i in range(1,bloques,1):
#        bloques = bloques - i
#        if bloques < 0:
#            continue
#        print(bloques)


bloques = int(input("Ingrese el número de bloques: "))
pisos = 0
usados = 1
while usados <= bloques:
    bloques -= usados
    usados += 1
    pisos += 1

print("La piramide tiene:", pisos, "pisos")
