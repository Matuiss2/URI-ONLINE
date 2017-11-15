while True:
    try:
        s = input()
    except EOFError:  # Tive que incluir isso pois o site tava dando esse erro
        break
    p = 0
    for c in s:  # Itera pela frase, cada loop é um letra(ou espaço)
        if c == ' ':
            print(c, end="")  # Se for um espaço não afeta a intercalação entre maiúscula e minúscula
        elif p == 0:  # Começa como maíuscula e intercala a cada letra(não considerando os espaços)
            print(c.upper(), end="")  # Converte a letra pra maiúscula  e junta tudo na mesma linha
            p += 1  # Muda o valor de p, fazendo intercalar entre as condições de if e else
        else:
            print(c.lower(), end="")  # Converte a letra pra minúscula e junta todos os prints na mesma linha
            p -= 1  # Muda o valor de p, fazendo intercalar entre as condições de if e else
    print()  # Tive que adicionar o espaço final pois estava dando erro