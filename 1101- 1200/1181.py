data = int(input())
op = input()
soma = 0
for horizontal in range(12):
    for vertical in range(12):
        valor = float(input())  # Pega os valores pela ordem horizontal
        if horizontal == data:  # Pega só os valores da linha escolhida para a operação
            soma += valor
if op == 'S':
    print(format(soma, ".1f"))
else:
    print(format(soma / 12.0, ".1f"))