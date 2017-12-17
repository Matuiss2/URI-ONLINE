maior = 0
maior_palavra = ""
while True:
    data = input().split()
    tamanho = []
    if data[0] == "0":
        break
    for i in data:
        tamanho.append(len(i))  # põe o tamanho de todas as palavras em uma lista
        if len(i) >= maior:  # Sempre troca a variável maior_palavra se a palavra atual é maior que a maior antes dela
            maior = len(i)
            maior_palavra = i
    print("-".join(map(str, tamanho)))  # transforma a lista de tamanhos em string e separa os itens por "-"
print()
print("The biggest word:", maior_palavra)