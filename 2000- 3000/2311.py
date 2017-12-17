loops = int(input())
for i in range(loops):
    nome = input()
    dificuldade = float(input())
    data = input().split()
    data_ordenada = sorted(map(float, data))  # tranforma os valores para float e ordena
    print(nome, format(sum(data_ordenada[1:-1]) * dificuldade, ".2f"))  # [1:-1] remove o maior e o menor valor