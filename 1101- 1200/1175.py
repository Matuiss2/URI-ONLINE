vetorinvertido = []
for i in range(20):
    data = int(input())
    vetorinvertido.append(data)  # junta os valores em uma lista
vetor = 0
for j in vetorinvertido[::-1]:  # inverte a lista
    print("N[{}] = {}".format(vetor, j))  # e imprime os valores em ordem inversa
    vetor += 1 # aumentando o vetor linha por linha
