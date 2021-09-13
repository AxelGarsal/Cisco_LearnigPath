rival = -999999
contador = 0

while True:
    jugador = int(input("Dame tu mejor numero: "))
    if jugador == -1:
        break
    contador = 1
    if jugador > rival:
        rival = jugador

if contador != 0:
    print("el nuevo rival es: ",rival)

# Otro código

while True:
    palabra = input('Rompe el hechizo: ')
    if palabra == 'chupacabra':
        break
print('Has salido del ciclo')
