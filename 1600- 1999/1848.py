# Converte os símbolos para decimal
valores = {"---": 0, "--*": 1, "-*-": 2, "*--": 4, "-**": 3, "*-*": 5,
           "**-": 6, "***": 7}
count = 0
while count != 3:  # Cada caw caw aumenta o valor em 1 e para no terceiro
    total = []  # Acumula todos os valores
    while True:
        data = input()
        total.append(data)
        if data == "caw caw":
            count += 1
            break
    # O caw caw também sempre entra na lista então se tiver 2 caw caw consecutivos vai entrar aqui e o valor será 0
    if len(set(total)) == 1:
        print(0)
    else:
        final = []
        # Sempre terá 1 caw caw no fim da lista então ele tem que ser removido
        total.remove("caw caw")
        for i in total:
            final.append(valores[i])  # junta os valores convertidos dos símbolos em uma lista
        print(sum(final))  # Soma todos os valores da lista