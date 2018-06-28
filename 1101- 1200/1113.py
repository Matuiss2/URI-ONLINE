while True:
    n1, n2 = map(int, input().split())
    if n1 == n2:
        break
    elif n1 > n2:
        print("Decrescente")
    else:
        print("Crescente")
