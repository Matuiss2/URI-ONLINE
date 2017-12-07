while True:
# Entrada
    vogais_a = input()  # Pega as vogais aliens já q tds as palavras e vogais são min, n preciso usar lower() ou upper()
    if vogais_a == "":  # Se estiver vazio fecha o programa
        break  # O while roda s parar qnd a cond for True, então só será interrompido qnd o break aparecer
    frase = input()  # Pega a frase a ser avaliada
    conta = 0  # Valor inicial para a contagem de vogais aliens na frase
# Processo
    for i in frase:  # Itera a frase letra por letra
        if i in vogais_a:  # Vê se a letra é uma das vogais aliens
            conta += 1  # Se for aumenta o contador em 1
# Saída
    print(conta)  # Imprime a qntd de vogais alien na palavra
