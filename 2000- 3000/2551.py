while True:
    try:
        dias = int(input())
    except EOFError:
        break
    maior = 0
    for i in range(dias):
        duracao, distancia = list(map(int, input().split()))
        if distancia / duracao > maior:
            print(i + 1)  # Imprime todos os dias em que o recorde foi batido
            maior = distancia / duracao  # Toda vez que o recorde for batido troca o valor de maior