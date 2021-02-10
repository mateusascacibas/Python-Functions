def KML(x,y):
    consumo = x/y

    if(consumo < 8):
        msg = "Venda o carro."
    elif(consumo <= 14):
        msg = "Economico."
    else:
        msg = "Super economico."
    return msg

KM = float(input("Digite a quantidade percorrida em KM: "))
Litros = float(input("Digite a quantidade de Litros gastos: "))

print(KML(KM,Litros))