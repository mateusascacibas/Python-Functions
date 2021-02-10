vet = list(range(5))


def vetor(vet):
    cont = 0
    maior = 0
    if cont == 0:
        maior = vet[cont]

    while cont < 5:
        if vet[cont] > maior:
            maior = vet[cont]
        cont +=1

    return maior

cont = 0

while cont < 5:
    vet[cont] = float(input("Digite um valor: "))
    cont += 1


print(vetor(vet))
