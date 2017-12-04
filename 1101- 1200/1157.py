numero = int(input())
for i in range(1, numero + 1):
    if numero % i == 0:  # Pega todos os divisores 1 por 1, não acho q seja o método mais eficiente mas é funcional
        print(i)
