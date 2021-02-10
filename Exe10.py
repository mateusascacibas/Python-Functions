def maior(a,b):

    if a > b:

        return "O maior é o " + format(a)
    elif b > a:
        return "O maior é o " + format(b)
    else:
        return "Iguais."

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

print(maior(numero1,numero2))
