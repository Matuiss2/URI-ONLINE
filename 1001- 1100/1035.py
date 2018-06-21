A, B, C, D = map(int, input().split())
if B > C and D > A and C + D > A + B and all(i > 0 for i in[C, D]) and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
