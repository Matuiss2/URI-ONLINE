loops = int(input())
for i in range(loops):
    data = input().split()
    numeros = input().split()
    if (int(numeros[0]) + int(numeros[1])) % 2 == 0:  # Checa se a soma é par
        if data[1] == "PAR":  # se a 1° pessoa escolheu par imprime o nome dela
            print(data[0])
        else:  # se não, imprime o nome da segunda pessoa
            print(data[2])
    else:  # Se for ímpar é só fazer a mesmo método, mudando as condições
        if data[1] == "IMPAR":
            print(data[0])
        else:
            print(data[2])
