leds = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}  # quantidade de leds dependendo do número
loops = int(input())  # Quantidade de loops
for i in range(loops):
    soma = 0
    valor = list(input())  # Pega o valor e separa cada número dentro de uma lista
    for v in valor:  # Pega 1 item da lista
        for d in leds:  # Pega os valores do dicionário leds
            if int(v) == d:  # Se o valor coincidir(sempre irá) entra aqui
                soma += leds[d]  # acumula o total de leds aqui, encontra o v no {leds} e retorna o valor correspondente
    print(soma, "leds")
