# Não acredito que seja a forma mais eficiente de fazer isso, pois tem muitas iterações
par = []
impar = []
for i in range(15):
    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if len(par) == 5:
        posicao = 0
        for j in par:
            print("par[{}] = {}".format(posicao, j))
            posicao += 1
        par = []
    if len(impar) == 5:
        posicao = 0
        for k in impar:
            print("impar[{}] = {}".format(posicao, k))
            posicao += 1
        impar = []

if len(impar) > 0:
    posicao = 0
    for l in impar:
        print("impar[{}] = {}".format(posicao, l))
        posicao += 1

if len(par) > 0:
    posicao = 0
    for m in par:
        print("par[{}] = {}".format(posicao, m))
        posicao += 1