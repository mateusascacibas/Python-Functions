def data(dia, mes, ano):
    mes_extenso = ""
    if mes == 1:
        mes_extenso = "janeiro"
    elif mes == 2:
        mes_extenso = "fevereiro"
    elif mes == 3:
        mes_extenso = "março"
    elif mes == 4:
        mes_extenso = "abril"
    elif mes == 5:
        mes_extenso = "maio"
    elif mes == 6:
        mes_extenso = "junho"
    elif mes == 7:
        mes_extenso = "julho"
    elif mes == 8:
        mes_extenso = "agosto"
    elif mes == 9:
        mes_extenso = "setembro"
    elif mes == 10:
        mes_extenso = "outubro"
    elif mes == 11:
        mes_extenso = "novembro"
    elif mes == 12:
        mes_extenso = "dezembro"
    else:
        mes_extenso = "Mês invalido. "

    return format(dia) + " de " + format(mes_extenso) + " de " + format(ano)


print(data(12,10,2020))