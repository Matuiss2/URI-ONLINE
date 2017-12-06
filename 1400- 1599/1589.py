loops = int(input())  # Pega o número de casos teste
for i in range(loops):
    data = input().split()  # Separa os números em itens de uma lista
    print(int(data[0]) + int(data[1]))  # Pega o primeiro número e soma pelo segundo(convertesse para int primeiro)
