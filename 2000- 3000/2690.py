# retorna o valor correspondente na tabela do enunciado e só retorna os primeiros 12 números
loops = int(input())
for i in range(loops):
    final = ""
    data = input()
    for j in data:
        if j in ["G", "Q", "a", "k", "u"]:
            final += "0"
        elif j in ["I", "S", "b", "l", "v"]:
            final += "1"
        elif j in ["E", "O", "Y", "c", "m", "w"]:
            final += "2"
        elif j in ["F", "P", "Z", "d", "n", "x"]:
            final += "3"
        elif j in ["J", "T", "e", "o", "y"]:
            final += "4"
        elif j in ["D", "N", "X", "f", "p", "z"]:
            final += "5"
        elif j in ["A", "K", "U", "g", "q"]:
            final += "6"
        elif j in ["C", "M", "W", "h", "r"]:
            final += "7"
        elif j in ["B", "L", "V", "i", "s"]:
            final += "8"
        elif j in ["H", "R", "j", "t"]:
            final += "9"
    print(final[:12])