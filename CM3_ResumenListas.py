# LISTAS
# 1. La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos.
# Es una colección ordenada y mutable de elementos separados por comas entre corchetes.
# 2. Las listas se pueden indexar y actualizar
# 3. Las listas pueden estar anidadas, por ejemplo: miLista = [1, 'a', ["lista", 64, [0, 1], False]].
# 4. Los elementos de la lista y las listas se pueden eliminar, por ejemplo:
# 5.Las listas pueden ser iteradas mediante el uso del bucle for
# 6. La función len() se puede usar para verificar la longitud de la lista
# 7. Una invocación típica de función tiene el siguiente aspecto:
# resultado = funcion(argumento), mientras que una invocación típica de un método se ve así: resultado = data.method(arg).
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
