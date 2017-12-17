# Se você souber as regras dos tipos de triangulo não é um exercício difícil, esse código pode ser simplificado tb
lados = list(map(int, input().split()))
A = lados[0]
B = lados[1]
C = lados[2]
if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print("Valido-Equilatero")
    elif A == B or B == C or C == A:
        print("Valido-Isoceles")
    elif A not in [B, C] or B not in [A, C] or B not in [A, C]:
        print("Valido-Escaleno")
    if A ** 2 == B ** 2 + C ** 2 or B ** 2 == A ** 2 + C ** 2 or C ** 2 == A ** 2 + B ** 2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
