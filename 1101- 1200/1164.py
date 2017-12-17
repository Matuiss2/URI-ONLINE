loops = int(input())
for i in range(loops):
    soma = 0
    data = int(input())
    for j in range(1, data):
        if data % j == 0:
            soma += j
    if soma == data:
        print(data, "eh perfeito")
    else:
        print(data, "nao eh perfeito")