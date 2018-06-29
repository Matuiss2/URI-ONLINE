for i in range(int(input())):
    inicial, proximos = map(int, input().split())
    total = 0
    for impares in range(inicial, inicial + (proximos * 2)):
        if impares % 2:
            total += impares
    print(total)
