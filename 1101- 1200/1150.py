n1 = int(input())
while True:
    n2 = int(input())
    if n2 > n1:
        break
soma = n1
qntd = 1
while True:
    if soma > n2:
        break
    soma += n1 + qntd
    qntd += 1

print(qntd)