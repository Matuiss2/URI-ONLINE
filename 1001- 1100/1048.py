salario = float(input())
aumentos = [0.15, 0.12, 0.1, 0.07, 0.04]
if salario <= 400:
    posicao = 0
elif salario <= 800:
    posicao = 1
elif salario <= 1200:
    posicao = 2
elif salario <= 2000:
    posicao = 3
else:
    posicao = 4
print("Novo salario: {}\nReajuste ganho: {}\nEm percentual: {} %".format(format(salario + salario * aumentos[posicao], ".2f"),
                                                                        format(salario * aumentos[posicao], ".2f"),
                                                                        int(aumentos[posicao] * 100)))
