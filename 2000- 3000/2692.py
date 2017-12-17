# põe os valores que serão trocados em um dicionário, troca esse valores por iteração e põe tudo na variável final
loops = list(map(int, input().split()))
trocas = {}
for i in range(loops[0]):
    letras = input()
    trocas[letras[0]] = letras[2]
    trocas[letras[2]] = letras[0]
for j in range(loops[1]):
    frase = input()
    final = ""
    for k in frase:
        if k in trocas.keys():
            final += trocas[k]
        else:  # se não for uma das chaves do dicionário mantem a letra
            final += k
    print(final)