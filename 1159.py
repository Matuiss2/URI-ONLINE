while True:
    data = int(input())
    total = 0
    if data == 0:
        break
    for i in range(data, data + 10):  # Inclúi o número + 4 pares(se for par) ou o número + 5 pares(se for impar)
        if i % 2 == 0:
            total += i
    print(total) 