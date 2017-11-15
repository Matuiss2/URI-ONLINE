# Entrada
loops = int(input())  # Qnt de iterações
for j in range(loops):
    texto = input()  # Todos os testes são maiusculos portanto não preciso converter usando upper()
    codigo = int(input())  # A quantidade a ser movida
    palavra = ""
# Processo
    if codigo == 0:  # Se for zero não terá modificações na palavra
        palavra += texto  # E retornará igual
    else:
        for i in texto:
            hop = ord(i) - codigo  # Pega o cod e checa o valor do símbolo covertido em ascii
            if hop < ord("A"):  # Se não corresponder à um símbolo dentro do alfabeto maiúsculo, vai entrar aqui
                hop += 26  # E dar a volta para correponder a uma letra correta seguindo em regras do exercício
            palavra += chr(hop)  # adiciona à variável palavra, as letras convertidas seguindo o código ascii
# Saída
    print(palavra)