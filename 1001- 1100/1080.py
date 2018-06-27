lista_numeros = []
for i in range(100):
    lista_numeros.append(int(input()))
print("{}\n{}".format(max(lista_numeros), lista_numeros.index(max(lista_numeros)) + 1))
