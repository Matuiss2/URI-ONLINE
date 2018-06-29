while True:
    numero = int(input())
    lista_numeros = []
    if numero == 0:
        break
    for i in range(1, numero + 1):
        lista_numeros.append(str(i))
    print(" ".join(lista_numeros))
