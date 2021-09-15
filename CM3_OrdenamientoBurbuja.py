lista = [8, 10, 6, 2, 4]
cambio = True
while cambio:
    cambio = False
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            cambio = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)


