while True:
    try:
        data = int(input())
    except EOFError:
        break
    final = []
    coluna = data - 1
    for i in range(data):
        principal = []
        for j in range(data):
            if j == coluna:
                principal.append(2)
                coluna -= 1
            else:
                if i == j:
                    principal.append(1)
                else:
                    principal.append(3)
        final.append(principal)
    for k in range(data):
        matriz = ''
        for l in range(data):
            matriz += str(final[k][l])
        print(matriz)