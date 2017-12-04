# Da para fazer a fórmula fatorial sem usar o built in também, e é relativamente fácil
# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
import math
while True:
    try:
        data = input().split()
    except EOFError:
        break
    print(math.factorial(int(data[0])) + math.factorial(int(data[1])))
