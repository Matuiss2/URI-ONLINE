quantidade = {}
for i in range(int(input())):
    data = int(input())
    # Toda vez que for contar a frequencia de todas as letras ou números usar esse método
    quantidade.setdefault(data, 0)  # se o item não estiver no dict coloca ela como chave e atribui o valor 0
    quantidade[data] = quantidade[data] + 1  # Cada vez q ele aperecer adiciona 1 ao valor
ordenado = sorted(quantidade.keys())
for j in ordenado:
    print("{} aparece {} vez(es)".format(j, quantidade[j]))