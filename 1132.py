num1 = int(input())
num2 = int(input())
total = 0
# Menor dos 2 como valor inicial e vai ate o maior o +1 é para incluir o proprio numero)
for i in range(min(num1, num2), max(num1, num2) + 1):
    if i % 13 != 0:  # Se não for divisível por 13 entra aqui
        total += i
print(total)