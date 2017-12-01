# Outro método seria incluir todas as jóias, mesmo as repetidas, na lista e imprimir set(len(lista_joias))
lista_joias = []
while True:
    try:
        joia = input()
    except EOFError:
        break
    if joia not in lista_joias:  # Se for uma jóia nova, ira entrar aqui
        lista_joias.append(joia)
print(len(lista_joias))  # Conta a quantidade de jóias distintas