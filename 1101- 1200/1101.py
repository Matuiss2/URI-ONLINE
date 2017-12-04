while True:
    data = input().split()
    total = 0
    menor = min(map(int, data))  # tranforma em int e pega o menor para poder entrar ordenado no in range()
    maior = max(map(int, data)) # tranforma em int e pega o maior para poder entrar ordenado no in range()
    if int(data[0]) <= 0 or int(data[1]) <= 0:  # Se for nulo ou negativo fecha o programa com o break
        break
    for i in range(menor, maior + 1):
        print(i, end=" ")  # concatena os números, dando um espaço entre eles
        total += i  # soma e acumula os números na variável total
    print("Sum="+str(total), end="")  # concaterna com o print de cima usando o end=""
    # Converti pra str pra grudar usando o +, s/ isso teria um espaço e daria presentation error
    print()  # Quebra a linha, resetando a concatenação do end=
