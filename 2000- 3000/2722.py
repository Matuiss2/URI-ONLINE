# Esse código é bem sujo e inficiente, da para melhorá-lo bastante
for i in range(int(input())):
    nome1 = input()
    nome2 = input()
    final = ""
    for j in range(max(len(nome1), len(nome2))):  # esse pegaria todos os casos, mas não é muito eficiente
        if j % 2 == 0:
            final += nome1[j:j+2] + nome2[j:j+2]
    print(final)