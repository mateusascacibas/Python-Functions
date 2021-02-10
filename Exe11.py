def media(n1,n2,n3,letra):
    media = 0.0

    if(letra == "A"):
        media = (n1 + n2 + n3) / 3
    elif(letra == "P"):
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    else:
        return "Erro. Letras aceitadas são A e P"

    return "A média é de {}".format(media)

cont = 1
vet = list(range(3))

while cont <= 3:
    vet[cont-1] = int(input("Digite a nota: "))
    cont += 1

letra = input("Digite A para media aritmetica e P para ponderada.")

print(media(vet[0],vet[1], vet[2], letra))

