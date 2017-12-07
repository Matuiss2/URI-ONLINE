# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    try:
        senha = input()
    except EOFError:
        break
    if len(senha) not in range(6, 33):  # Eliminando casos erroneos(deixa o programa mais rápido)
        print("Senha invalida.")
    else:
        maiuscula = 0
        minuscula = 0
        numeral = 0
        for i in senha:  # Pega letra por letra (não é um método mto eficiente, mas faz o trabalho)
            if i.isupper():  # Se for maiúscula entra aqui e acrescenta a quantidade na variável
                maiuscula += 1
            elif i.islower():  # Se for minúscula entra aqui e acrescenta a quantidade na variável
                minuscula += 1
            elif i.isdecimal():  # Se for numeral entra aqui e acrescenta a quantidade na variável
                numeral += 1
            else:  # for um espaço ou símbolo entre aqui e fecha
                print("Senha invalida.")
                break
        else:  # Se o loop não for quebrado pelo break entra aqui(método exclusivo do python for - else)
            if minuscula == 0 or maiuscula == 0 or numeral == 0:  # se não ter tds desses tipos na senha ela é inválida
                print("Senha invalida.")
            else:  # Se cumpriu com todos os requesitos, entra aqui
                print("Senha valida.")
