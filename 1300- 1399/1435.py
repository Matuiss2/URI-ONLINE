while True:
    data = int(input())
    if data == 0:
        break
    matriz_final = []
    for i in range(data):
        um = []
        for j in range(data):
            um.append(1)
        matriz_final.append(um)
    valor = 1
    topo = 0
    lado1 = 0
    bot = data - 1
    lado2 = data - 1
    if data % 2 == 0:
        meio = data / 2
    else:
        meio = data + 1 / 2
    while valor <= meio:
        i = lado1
        while i <= lado2:
            matriz_final[topo][i] = valor
            matriz_final[bot][i] = valor
            i += 1
        i = (topo + 1)
        while i < bot:
            matriz_final[i][lado1] = valor
            matriz_final[i][lado2] = valor
            i += 1
        valor += 1
        topo += 1
        bot -= 1
        lado1 += 1
        lado2 -= 1
    for i in range(data):
        tx = ''
        for j in range(data):
            if j == data - 1:
                # essa linha da muito trabalho quanto a PE no site(n use format() nesse caso)
                tx += " %3d".format(matriz_final[i][j])
        print(tx[1:])
    print()