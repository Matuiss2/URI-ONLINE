n1, n2 = int(input()), int(input())
for numeros in range(min(n1, n2) + 1, max(n1, n2)):
    if numeros % 5 in [2, 3]:
        print(numeros)
