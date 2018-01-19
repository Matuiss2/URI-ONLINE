while True:
    data = input()  # negativos fecham o programa, poderia converter para int primeiro mas esse método é mais eficiente
    if data.startswith("-"):
        break
    if data.startswith("0x"):  # 0x idetifica numeros hexadecimais
        print(int(data, 16))  # esse método ignora automaticament o 0x
    else:
        """ hex converte para hexadecimal incluindo 0x, mas em letras minúsculas
         o exercício pede em letra máisculas(tirando o X de 0x), por isso o
         método upper e replace"""
        print(hex(int(data)).upper().replace("X", "x"))