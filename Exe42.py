vet = list(range(5))


def vetor(vet):
    cont = 0
    soma = 0.0
    media = 0.0
    while cont < 5:
        soma += vet[cont]
        cont +=1

    media = soma / 5
    return media

cont = 0

while cont < 5:
    vet[cont] = float(input("Digite um valor: "))
    cont += 1


print(vetor(vet))
