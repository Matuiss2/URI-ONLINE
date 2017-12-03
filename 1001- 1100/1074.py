loops = int(input())
for i in range(loops):
    p_i = ""
    data = int(input())
    if data == 0:
        p_i += "NULL"
    elif data % 2 == 0:
        p_i += "EVEN " # Adicionar o espaço aqui no final para não dar presentation error
    else:
        p_i += "ODD "  # Adicionar o espaço aqui no final para não dar presentation error
    if data > 0:
        p_i += "POSITIVE"
    elif data < 0:
        p_i += "NEGATIVE"
    else:
        pass
    print(p_i)
