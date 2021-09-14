numeros = [1, 5, 9, 14, 22, 130]
print(numeros)
numeros[0] = -66
numeros[5] = -666
numeros[3] = -66
print(numeros)
numeros[4]=numeros[1]
print(numeros)
print('La lista tiene', len(numeros), 'elementos')
# len() es un función, para eliminar un elemento podemos usar una instrucción llamada 'del'
del numeros[3]
print(numeros)
print('La lista tiene', len(numeros), 'elementos')
# la indexación puede ir en sentido inverso
print('el último número es: ', numeros[-1])
