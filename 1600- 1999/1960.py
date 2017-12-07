# Dava para fazer com o método de dicionário, mas assim funciona tb
def num_romanos(restando):
    numeros = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    romanos = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(13):  # 13 valores chave
        count = restando // numeros[i]
        result += romanos[i] * count
        restando -= numeros[i] * count
    return result


pagina = int(input())
print(num_romanos(pagina))
