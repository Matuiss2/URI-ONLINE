# O a adicional nas variaveis representa os acertos, é nescessário saber o total e os acertos para calcular a %
loops = int(input())
totals = 0
totalb = 0
totala = 0
totalsa = 0
totalba = 0
totalaa = 0
for i in range(loops):
    nome = input()
    data = input().split()
    saque, block, attack = int(data[0]), int(data[1]), int(data[2])
    data2 = input().split()
    saquea, blocka, attacka = int(data2[0]), int(data2[1]), int(data2[2])
    totals += saque
    totalb += block
    totala += attack
    totalsa += saquea
    totalba += blocka
    totalaa += attacka
print("Pontos de Saque:", format(totalsa / totals * 100, ".2f"), "%.")  # format(valor, ".2f) arredonda em 2 casas dec
print("Pontos de Bloqueio:", format(totalba / totalb * 100, ".2f"), "%.")
print("Pontos de Ataque:", format(totalaa / totala * 100, ".2f"), "%.")
