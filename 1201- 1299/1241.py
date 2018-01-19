# Identico ao 1240
for i in range(int(input())):
    a, b = input().split()
    if len(b) > len(a):
        print("nao encaixa")
    elif b == a[-len(b):]:
        print("encaixa")
    else:
        print("nao encaixa")