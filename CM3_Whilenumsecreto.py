numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
adivina = int(input('Ingresa el que crees que es el número secreto: '))
while adivina != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!" )
    adivina = int(input('ingresa otro numero: '))
    if adivina == numeroSecreto:
        print("¡Bien hecho, muggle! Eres libre ahora")
