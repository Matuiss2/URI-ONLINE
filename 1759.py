numero = int(input())
str_i = ""
for i in range(numero):
    str_i += "Ho "  # Junta ho e um espaço na variável str_i pelo número determinado
print(str_i[:-1] + "!")  # No fim elimina o último espaço usando o slice e adiciona o ! no fim
