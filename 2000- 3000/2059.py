# O valor de r e a são prioridade, só é preciso checar o valor de par ou ímpar se eles forem 0
p, j1, j2, r, a = map(int, input().split())
total = (j1 + j2) % 2
if r == 0:
    if a == 0:
        if (total == 0 and p == 1) \
        or (total == 1 and p == 0):
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")
elif r == 1:
    if a == 0:
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")