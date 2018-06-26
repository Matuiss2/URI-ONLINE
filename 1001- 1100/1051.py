if 0 < salario <= 2000:
    print("Isento")
else:
    if 2000 < salario <= 3000:
        imposto = (salario - 2000) * 0.08
    elif 3000 < salario <= 4500:
        imposto = 80 + (salario - 3000) * 0.18
    else:
        imposto = 350 + (salario - 4500) * 0.28
    print("R$", format(imposto, ".2f"))
