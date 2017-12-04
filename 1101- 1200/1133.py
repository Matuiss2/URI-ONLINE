a = int(input())
b = int(input())
for i in range(min(a, b) + 1, max(a, b)):  # itera os numeros entre o menor valor e o maior n incluindo eles mesmos.
    if i % 5 == 2 or i % 5 == 3:
        print(i)  # Imprime quando o numero for dividido por 5 e sobrar 2 ou 3 depois da operacao
