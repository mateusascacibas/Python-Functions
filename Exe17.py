def soma(x,y):
    soma = 0

    while(x < y):
        soma += x
        x += 1

    return soma

print(soma(5,10))