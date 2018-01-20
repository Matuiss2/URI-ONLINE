a, b, c = list(map(int, input().split()))
if a in [b, c] or b == c or a == b + c or b == a + c or c == a + b:
    print("S")
else:
    print("N")