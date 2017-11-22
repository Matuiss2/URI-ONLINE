idade = 1  # Valor para determinar idade como int não será contabilizado
qnt = 0
total_idade = 0
while idade > 0:
    idade = int(input())
    if idade > 0:  # Valor de fechamento(negativos) não serão contabilizados
        total_idade += idade
        qnt += 1
print(format(total_idade / qnt, ".2f"))