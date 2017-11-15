# Entrada
loops = int(input())  # Recebe o número de mensagens que o programa vai receber
for l in range(loops):  # Faz iteração por determinado número de vezes(o número que estiver no loops)
    palavra = input()  # Recebe a mensagem a ser criptografada
    palavra1 = ""  # Armazena em uma variável a mensagem depois de primeira etapa da criptografia
# Processo
    for letter in palavra:  # Itera a entrada inicial (cada iteração é uma letra)
        if letter.isalpha():  # Se for letra vai ser True(se não for letra vai ser false)
            palavra1 += chr(ord(letter) + 3)  # chr(ord(letter), identifica o valor ASCII da letra e retorna 3 a frente
        else:
            palavra1 += letter  # Se for símbolo ou número irá se manter nessa etapa
    palavra_inversa = palavra1[::-1]  # [::-1] Inverte a palavra concluindo a primeira etapa da criptografia
    metade_truncada = len(palavra1) // 2   # Identifica quando chega na metade truncada da palavra
    palavra_final = palavra_inversa[:metade_truncada]  # Pega o início até a metade da palavra q deve permanecer igual
    for letter in palavra_inversa[metade_truncada:]:   # Pega da metade até o final para modificar
        palavra_final += chr(ord(letter) - 1)  # chr(ord(letter), ident o val ASCII do simb/letra e passa ele 1 pra tras
# Saída
    print(palavra_final)  # imprime o valor final
