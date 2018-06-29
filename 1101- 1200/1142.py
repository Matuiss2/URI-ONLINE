inicial = 1
for i in range(int(input())):
    lista_numeros = []
    for j in range(3):
        lista_numeros.append(inicial + j)
    inicial += 4
    print(" ".join(map(str, lista_numeros)), "PUM")
