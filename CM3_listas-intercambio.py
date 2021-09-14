# Paso 1: Crea una lista vacía llamada beatles.
# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
# Paso 3: Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles = []

for i in range(5):
    beatles.append(input('Dame el beatle: '))
print(beatles)
del beatles[3]
del beatles[3]
print(beatles)
beatles.insert(0,'Ringo Star')
print(beatles)
