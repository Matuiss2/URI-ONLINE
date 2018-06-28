while True:
    data = list(map(int, input().split()))
    menor, maior, total = min(data), max(data), []
    if any(j <= 0 for j in data):
        break
    for i in range(menor, maior + 1):
        total.append(i)
    print("{} Sum={}".format(" ".join(map(str, total)), sum(total)))
