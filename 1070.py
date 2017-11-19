data = int(input())
for i in range(12):  # 12 pois inclui os pares
    if data % 2 != 0:
        print(data)
    data += 1 