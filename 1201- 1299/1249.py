# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        data = input()
    except EOFError:
        break
    final = ""
    for i in data:
        if i.isalpha():  # se for uma letra entra aqui
            character = ord(i) + 13  # ord retorna o código numérico ASCII de um simbolo
            if i.isupper():  # Se a letra for maiúscula entra qui
                if character > 90:  # Se sair do alfabeto maiúsculo ASCII...
                    character -= 26 # ...vai dar a volta e entrar de novo no alfabeto
                final += chr(character)  # chr retorna o símbolo equivalente a um código numérico de acordo com ASCII
            else:  # Faz a mesma coisa que antes só q agora com as minúsculas
                if character > 122:
                    character -= 26
                final += chr(character)
        else:  # Se for um símbolo ou número não ocorre alterações
            final += i
    print(final)