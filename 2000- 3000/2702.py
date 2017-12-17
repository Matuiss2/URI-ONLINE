# pega a diferença entre as refeições disponíveis e pedidas e soma todas os pedidos não completos
refeicoes = list(map(int, input().split()))
pedidos = list(map(int, input().split()))
total = 0
if refeicoes[0] < pedidos[0]:
    total += abs(refeicoes[0] - pedidos[0])
if refeicoes[1] < pedidos[1]:
    total += abs(refeicoes[1] - pedidos[1])
if refeicoes[2] < pedidos[2]:
    total += abs(refeicoes[2] - pedidos[2])
print(total)