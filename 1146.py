while True:  # O programa vai rodar até chegar no break
    numero = int(input())
    if numero == 0:
        break  # se for 0 o programa para
    final = ""  # string inicial
    if numero:
        for i in range(1, numero + 1):
            final += str(i)+" "  # O método mais eficiente aqui é o "".join(i), mas esse é + conhecido então usei ele
    print(final[:-1])  # Remove o espaço final 