while True:
    a, b, c, d = list(map(int, input().split()))
    if a + b + c + d == 0:
        break
    if a == c and b == d:
        print(0)
    elif a + b == c + d or a - b == c - d or a == c or b == d:
        print(1)
    else:
        print(2)