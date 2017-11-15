# Entrada
n = int(input())
for i in range(n):
    a = input().replace("·", " ")  # Troca os pontos por um espaço vazio
    a = a.split()  # Separa as palavras que estão divididas pelo parametro(nesse caso o espaço vazio)
    texto = ""  # Texto inicial
# Processo
    for p in a:  # Divide a lista ou string por item(nesse caso cada palavra é um item por causa do split)
        texto += p[0]  # Pega a primeira letra de cada palavra e acumula no texto
# Saída
    print(texto)  # Imprime a resposta