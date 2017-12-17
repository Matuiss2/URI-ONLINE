loops = int(input())
data = input().split()
final = ""
for j in data:
    if j[:2] in ["OB", "UR"] and len(j) == 3:  # vê se começa com OB ou UR e se tem 3 de tamanho
        final += j[:2] + "I" + " "  # tiver elimina a outra letra e substitui por i (separando cada 1 por espaços)
    else:
        final += j + " "  # se não for mantêm a palavra, separando por espaços
print(final[:-1])  # remove o último espaço