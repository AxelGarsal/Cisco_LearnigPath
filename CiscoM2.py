print('hola','soy','Axel',sep=' ',end='* ')
print('Esto','lo','aprendi','de','CiscoAcademy',sep='_',end='*')
# reto
print("  *****"*2)
# Notación Científica
print(3E8) # 3x10^8
print(0o123)
print(0x123)
print(6.62607E-34)
print(0.0000000000000000000001)
print("Me gusta\n \"Monty Python\"\n" )
print("Estoy\n\"aprendiendo\"\n\"\"\"Python\"\"\"")

print(True > False)
print(True < False < None)
var = 1
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)
# convertidor de millas a kilometros
km = 12.25
mll = 7.38
# km a millas
nuevaMll = mll * 1.61
nuevoKm = km/1.61
print("Los", km,"Kilometros A millas son", round(nuevaMll,2))
print("Las", mll,"Millas a kilometros son", round(nuevoKm,1))

# Función Hipotenusa
cA = float(input("Valor de Cateto Adyacente: "))
cO = float(input("Valor de Opuesto Adyacente: "))
hipo = (cA**2 + cO**2)
print(hipo)
# Cuadro con caracteres
print("+" + 10*"-"+'+')
print(("|"+ 10*" "+'|\n')*5,end='')
print("+" + 10*"-"+'+')
# operacion de fracción anidada
x = float(input("Ingresa el valor para x: "))

# coloca tu código aquí
y = 1/( x+1/(x+1/(x+(1/x)))  )

print("y =", y)


x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)



