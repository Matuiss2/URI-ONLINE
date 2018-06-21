inicio, fim = map(int, input().split())
if inicio >= fim:
    print("O JOGO DUROU {} HORA(S)".format(abs(inicio - 24) + fim))
else:
    print("O JOGO DUROU {} HORA(S)".format(fim - inicio))
