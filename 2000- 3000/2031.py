valor = {"ataque": 3, "pedra": 2, "papel": 1 }
for i in range(int(input())):
    jog1 = valor[input()]  # converte para o valor correspondente do dicionário automaticamente
    jog2 = valor[input()]
    if jog1 == jog2:
        if jog1 == 1:
            print("Ambos venceram")
        elif jog1 == 2:
            print("Sem ganhador")
        else:
            print("Aniquilacao mutua")
    elif jog1 > jog2:
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")