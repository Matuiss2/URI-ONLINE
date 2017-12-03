salario = float(input())
if salario <= 400:
    novo_salario = salario * 1.15
    ep = "15 %"
elif salario <= 800:
    novo_salario = salario * 1.12
    ep = "12 %"
elif salario <= 1200:
    novo_salario = salario * 1.1
    ep = "10 %"
elif salario <= 2000:
    novo_salario = salario * 1.07
    ep = "7 %"
else:
    novo_salario = salario * 1.04
    ep = "4 %"
print("Novo salario:", format(novo_salario, ".2f"))
print("Reajuste ganho:", format(novo_salario - salario, ".2f"))
print("Em percentual:", ep)
