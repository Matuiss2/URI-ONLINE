pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    data = int(input())
    if data % 2 == 0:
        pares += 1
    else:
        impares += 1
    if data > 0:
        positivos += 1
    elif data < 0:
        negativos += 1
print(pares, "valor(es) par(es)")
print(impares, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")
