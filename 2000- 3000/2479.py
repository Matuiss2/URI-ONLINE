lista_nomes = []
bons = 0
ruins = 0
for i in range(int(input())):
    comportamento, nomes = input().split()
    lista_nomes.append(nomes)
    if comportamento == "+":
        bons += 1
    else:
        ruins += 1
print("\n".join(sorted(lista_nomes)))  # Põe a lista do nomes em ordem e separa cada um deles por linha
print("Se comportaram: {} | Nao se comportaram: {}".format(bons, ruins))