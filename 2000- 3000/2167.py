# Dá para reduzir esse código e dá para usar o método lista.index() tb
qnt = int(input())
data = input().split()
posicao = 1
maior = 0
for i in map(int, data):
    if i >= maior:
        maior = i
        posicao += 1
    else:
        print(posicao)
        break
else:
    print(0)