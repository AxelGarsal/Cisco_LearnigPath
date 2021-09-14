# Lista de mayor a menor
# el método .insert() puede agregar un elemento en cualquier posición de la lista
mi_lista = []
for i in range(1,11,1):
    mi_lista.insert(0,i)
print(mi_lista)

# Lista de menor a mayor
# El método .append() solo puede agregar un elemento al inicio de la lista
lista_menor = []
for i in range(11):
    lista_menor.append(i)
print(lista_menor)

# Sumar elementos de una lista
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)

# otra manera de sumar elementos de una lista
lista_sum = [1, 55, 6, 13, -36]
sumas = 0
for i in lista_sum:
    sumas = sumas + i
print(sumas)

