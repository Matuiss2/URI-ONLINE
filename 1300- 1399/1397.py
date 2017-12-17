while True:
    loops = int(input())
    if loops == 0:
        break
    jogador1 = 0
    jogador2 = 0
    for i in range(loops):
        data = list(map(int, input().split()))  # transforma os input em int() e põe numa lista
        if data[0] > data[1]:  # O maior número recebe 1 ponto
            jogador1 += 1
        elif data[1] > data[0]:
            jogador2 += 1
    print("{} {}".format(jogador1, jogador2))