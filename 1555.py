# Essa questão era só traduzir para python as fórmulas de cada 1
loops = int(input())  # Vê a qntd de casos testes
for i in range(loops):
    data = input().split()
    x, y = int(data[0]), int(data[1])
    raf = (3 * x) * (3 * x) + (y * y)
    bet = 2 * (x * x) + (5 * y) * (5 * y)
    car = -100 * x + (y * y * y)
    if raf > bet and raf > car:
        print("Rafael ganhou")
    elif car > bet and car > raf:
        print("Carlos ganhou")
    else:
        print("Beto ganhou")