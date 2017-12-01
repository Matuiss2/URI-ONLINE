# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        data = int(input())  # Número de votantes
    except EOFError:
        break
    dois_tercos = data * 2 / 3  # Identifica quanto é 2/3 de todos os votos
    votos = input().split()
    total = sum(map(int, votos))  # Transforma os itens da list em int e retorna e soma de todos
    if total >= dois_tercos:
        print("impeachment")
    else:
        print("acusacao arquivada")