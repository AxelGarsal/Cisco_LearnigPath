# Tu programa debe:
# Pedir al usuario que ingrese una palabra.
# Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas;
# hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales
# A , E , I , O , U de la palabra ingresada.
# Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

palabra = input('dame tu palabra: ')
palabra = palabra.upper()
for letra in palabra:
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        continue
    print(letra)

# ahora imprime la palabra sin vocales
sinvocal = ''
palabra2 = input('dame tu palabra: ')
palabra2 = palabra2.upper()
for letra in palabra2:
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        continue
    sinvocal = sinvocal + letra
print(sinvocal)


