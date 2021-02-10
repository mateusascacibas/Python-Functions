def efetue(x, y, z):
    tentativa = 1

    if(z == "*"):
        count = x * y
    elif(z == "+"):
        count = x + y
    elif(z == "-"):
        count = x - y
    elif(z == "/"):
        if(x != 0 and y != 0):
            count = x / y
        else:
            tentativa = 0
            return "Divisão por 0 não existe."
    else:
        tentativa = 0
        return "Digite um sinal de conta válido."

    if(tentativa == 1):
        return "O resultado da operação " + format(x) + " " + format(z) + " " + format(y) + " é de: " + format(count)


x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))
z = input("Digite +, -, / ou * para realizar a conta. ")

print(efetue(x,y,z))