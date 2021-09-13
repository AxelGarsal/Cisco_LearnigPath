#Usando uno de los operadores de comparación en Python, escribe un programa simple
#de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime
#False si n es menor que 100, y True si n es mayor o igual que 100

n = int(input('tu número: '))
print("n es menor que 100 ", n < 100)
print("n es mayor o igual a 100 ", n >= 100)

# Número más grande comparación:
n1 = int(input('tu numero: '))
n2 = int(input('tu numero: '))

if n1 > n2:
    n3 = n1
else:
    n3 = n2

print('El numero mas grande es: ', n3)
