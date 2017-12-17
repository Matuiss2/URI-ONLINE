# Muito ineficiente mas é aceito, revisitando esse código eu fiquei com vergonha, tem um jeito MT + simples de fazê-lo
nome = []
while True:
    try:
        nomes = input()
    except EOFError:
        break
    nome.append(nomes)
    minusculos = [i.lower() for i in nome]
    ultimo = minusculos.index(max(minusculos))
print(nome[ultimo])