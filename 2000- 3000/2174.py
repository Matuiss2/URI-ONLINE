loops = int(input())
lista1 = []
for i in range(loops):
    pomekon = input()
    lista1.append(pomekon)
tamanho = len(set(lista1))
print("Falta(m)", 151 - tamanho, "pomekon(s).")
