# Esse ex é um pouco diferente em python, td o q vc precisa fazer é modificar o % e // para que funcionem q nem no C++
data = input().split()
a = int(data[0])
b = int(data[1])
div = divmod(a, abs(b))
if b < 0:
    print(- div[0], div[1])
else:
    print(div[0], div[1])