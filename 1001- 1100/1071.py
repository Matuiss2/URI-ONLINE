numero_inicial, numero_final = int(input()), int(input())
maior, menor = max(numero_final, numero_inicial), min(numero_final, numero_inicial)
soma = 0
for impares in range(menor + 1, maior):
    if impares % 2:
        soma += impares
print(soma)
