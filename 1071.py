num1 = int(input())
num2 = int(input())
maior = max(num1, num2)  # Pega o maior valor entre os 2, para ser o valor final para o for()
menor = min(num1, num2)  # Pega o menor valor entre os 2, para ser o valor inicial no for()
soma = 0
for i in range(menor + 1, maior):  # Não pode incluir os próprios números por isso o + 1
    if i % 2 != 0:
        soma += i
print(soma)
