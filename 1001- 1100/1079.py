for i in range(int(input())):
    n1, n2, n3 = map(float, input().split())
    print(format((n1 * 2 + n2 * 3 + n3 * 5) / 10, ".1f"))
