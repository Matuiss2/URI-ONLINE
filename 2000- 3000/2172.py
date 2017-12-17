while True:
    data = input().split()
    if int(data[0]) + int(data[1]) == 0:
        break
    print(int(data[0]) * int(data[1]))
