data = input().split()
inicio = int(data[0])
final = int(data[1])
if inicio >= final:  # se forem dias diferentes incluí 24 h(um dia) na conta
    print("O JOGO DUROU", abs(inicio - final - 24), "HORA(S)")
else:
    print("O JOGO DUROU", final - inicio, "HORA(S)")