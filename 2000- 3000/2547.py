while True:
    try:
        loops, menor, maior = list(map(int, input().split()))
    except EOFError:
        break
    qnt = 0
    for i in range(loops):
        tamanho = int(input())
        if tamanho in range(menor, maior + 1):  # +1 para incluir o próprio número
            qnt += 1  # conta a qnt de pessoas que estão no range de altura
    print(qnt)