andares = []
for i in range(3):
    data = int(input())
    andares.append(data)
# calcula o tempo que será gasto dependendo de que posição a máquina está
primeiro = 2 * andares[1] + 4 * andares[2]
segundo = 2 * andares[0] + 2 * andares[2]
terceiro = 4 * andares[0] + 2 * andares[1]

print(min(primeiro, segundo, terceiro))  # imprime o menor dos valores