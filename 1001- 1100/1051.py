salario = float(input())
# Todos os val subtraem o salário max anterior e soma o valor máximo possível acumulado nas etapas anteriores
if 0 < salario <= 2000:
    print("Isento")
elif 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print("R$", format(imposto, ".2f"))
elif 3000 < salario <= 4500:
    imposto = 80 + (salario - 3000) * 0.18
    print("R$", format(imposto, ".2f"))
else:
    imposto = 350 + (salario - 4500) * 0.28
    print("R$", format(imposto, ".2f"))
