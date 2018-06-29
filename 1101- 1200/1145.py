tamanho, maximo = map(int, input().split())
inicial = 0
while inicial < maximo:
    lista_numeros = []
    for i in range(tamanho):
        inicial += 1
        if inicial <= maximo:
            lista_numeros.append(str(inicial))
    print(" ".join(lista_numeros))
