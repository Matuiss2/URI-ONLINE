# Entrada
import math
T = int(input())
for i in range(T):
    numeros = input().split()  # Pega os valores do input e separa
    PA = int(numeros[0])  # População 1° cidade
    PB = int(numeros[1])  # População 2° cidade
    G1 = float(numeros[2])  # Taxa de crescimento da 1° cidade em %
    G2 = float(numeros[3])  # Taxa de crescimento da 2° cidade em %
    anos = 0  # Valor inicial para os anos
# Processo
    while PA <= PB:  # O exercício diz alcançar e não ultrapassar portanto o condição é <=
        anos += 1  # Cada iteração aumenta o valor em 1 ano
        if anos > 100:  # Se durar mais de 1 século para alcançar a população quebra o loop
            break
        else:
            PA += math.floor(PA * G1 / 100)  # arredonda para baixo seguindo as instruções do exercício
            PB += math.floor(PB * G2 / 100)  # arredonda para baixo seguindo as instruções do exercício
# Saída
    if anos > 100:  # Se demorar mais que 100 anos imprime isso
        print("Mais de 1 seculo.")
    else:
        print(anos, "anos.") 