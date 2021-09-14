# intercambiar valores en una lista
lista = [10, 1, 8, 3, 5]
print(lista)
lista[0],lista[4],lista[1],lista[3] = lista[4],lista[0],lista[3],lista[1]
print(lista)


# intercambio de lugares con for
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)
print(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista)
