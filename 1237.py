def longest_common_substr_length(s1, s2):
# Processo
    substr_len = min(map(len, (s1, s2)))
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    for length in range(substr_len, 0, -1):
        for index in range(0, len(s1)-length+1):
            if s1[index:index+length] in s2:
                return length
    return 0


a = "bla"
b = "bla"
while a != "" and b != "":
# Entrada
    try:
        a = input()
        b = input()
# Saída
        if a and b:
            print(longest_common_substr_length(a, b))
        else:
            break
    except EOFError:
        break