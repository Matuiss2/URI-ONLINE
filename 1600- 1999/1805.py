inicio, fim = list(map(int, input().split()))
""" Para achar a qntd de termos --- final = inicial + (qntd - 1) * razao 
no caso desse exercício isso será sempre qntd = fim - inicio + 1
A soma de todos os naturais em um intervalo é:
(inicial + final) + qntd de termos / 2"""
final = (inicio + fim) * (fim - inicio + 1) / 2  # juntei tudo nessa fórmula
print(int(final))