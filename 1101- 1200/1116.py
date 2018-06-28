for i in range(int(input())):
    cima, baixo = map(float, input().split())
    if baixo == 0:
        print("divisao impossivel")
    else:
        print(format(cima / baixo, ".1f"))