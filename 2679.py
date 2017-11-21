numero = int(input())
# Não pode incluir o proprio número por isso o + 1, o + 3, é para incluir os 2 proximos números (1 deles será par)
for i in range(numero + 1, numero + 3):
    if i % 2 == 0:  # se for par imprime o número e fecha o programa
        print(i)
        break