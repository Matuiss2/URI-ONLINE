# convertido da resposta de Matheus Glauber
while True:
    matriz = []
    col = 0
    qtd = int(input())
    if qtd == 0:
        break
    elif qtd > 1:
        valor = 1
        for i in range(qtd):
            linha = []
            for l in range(qtd):
                linha.append(valor)
                valor *= 2
            matriz.append(linha)
            valor = matriz[col][1]
            col += 1
        tamanho = len(str(matriz[-1][-1]))
    if qtd == 1:
        print(qtd)
    else:
        for linha in matriz:
            for elemento in range(qtd):
                if elemento < qtd - 1:
                    print('{:{}}'.format(linha[elemento], tamanho), end=' ')
                else:
                    print('{:{}}'.format(linha[elemento], tamanho))
    print()