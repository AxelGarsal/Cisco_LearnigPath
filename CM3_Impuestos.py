# Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos
# (esta fue la llamada exención fiscal ).
# Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
# Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero,
# solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

ingreso = float(input("Cuál es tu ingreso anual?: "))

if ingreso >1 and ingreso <= 85526:
    ipi = (ingreso*.18) - 556.2
    print("Tu impuesto IPI asciende a la cantidad de: ",round(ipi,0))
elif ingreso <= 0:
    print("No tiene que pagar impuestos!")
else:
    excedente = ingreso - 85528
    ipi = 14839.2 + (excedente*.32)
    print("Tu impuesto IPI asciende a la cantidad de: ",round(ipi,0))
