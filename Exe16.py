def linhas(x):
    cont = 0
    linha = ""
    while cont < x:
        linha += "="
        cont += 1

    return linha

l = int(input("Quanto de comprimento tem sua linha? "))

print(linhas(l))