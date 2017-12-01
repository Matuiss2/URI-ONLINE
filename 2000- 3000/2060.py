loops = int(input())
data = input().split()
dois = 0
tres = 0
quatro = 0
cinco = 0
for j in map(int, data):  # transforma os valores da lista data em int
    # E checa a qntd de divisiveis de 2, 3, 4, 5 nessa lista
    if j % 2 == 0:
        dois += 1
    if j % 4 == 0:
        quatro += 1
    if j % 3 == 0:
        tres += 1
    if j % 5 == 0:
        cinco += 1
print(dois, "Multiplo(s) de 2")
print(tres, "Multiplo(s) de 3")
print(quatro, "Multiplo(s) de 4")
print(cinco, "Multiplo(s) de 5")
