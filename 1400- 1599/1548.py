for i in range(int(input())):
    alunos = int(input())
    notas = list(map(int, input().split()))  # pega as notas e põe em uma lista desordenada
    notas_ordenadas = sorted(notas, reverse=True)  # ordena as notas da maior para menor
    total = 0
    for j in range(alunos):
        # Se a nota do aluno estiver na mesma posição em que ele chegou aumenta o resultado em 1
        if notas[j] == notas_ordenadas[j]:
            total += 1
    print(total)