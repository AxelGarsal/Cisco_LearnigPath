# Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:
# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.

year = int(input('Ingresa el año de tu interés: '))
if year <= 1582:
    print("El año",year,"no entra calendario Gregoriano")
elif year % 4 != 0:
    print("El año",year,"Es común")
elif year % 100 != 0:
    print("El año",year,"es bisiesto")
elif year % 400 != 0:
    print("El año",year,"es común")
else:
    print("El año",year,"es bisiesto")
