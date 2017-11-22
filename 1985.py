loops = int(input()) # Vê a qntd de casos testes
total = 0
for i in range(loops):
    data = input().split()
    if data[0] == "1001":  # Data[0] é o item, Data[1] a qntd
        total += 1.5 * int(data[1])
    elif data[0] == "1002":
        total += 2.5 * int(data[1])
    elif data[0] == "1003":
        total += 3.5 * int(data[1])
    elif data[0] == "1004":
        total += 4.5 * int(data[1])
    elif data[0] == "1005":
        total += 5.5 * int(data[1])
print(format(total, ".2f"))