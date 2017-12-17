# Poderia ser feito por regex, mas eu acho que nesse caso específico seria mais complicado
data = input()
vogais = []
for char in data:
    if char in ["a", "e", "i", "o", "u"]:
        vogais.append(char)
if vogais == vogais[::-1]:  # Só se as vogais formarem um palíndromo que imprime "S"
    print("S")
else:
    print("N")