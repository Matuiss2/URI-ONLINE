for i in range(int(input())):
    data = map(int, input().split())
    maior, menor, soma_impares = max(data), min(data), 0
    for j in range(menor + 1, maior):
        if j % 2:
            soma_impares += j
    print(soma_impares)
