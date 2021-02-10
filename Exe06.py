def seg(hora, minuto, segundo):
    minuto_acumulado = hora * 60
    segundo_acumulado = (minuto_acumulado + minuto) * 60
    segundo_final = segundo_acumulado + segundo

    return segundo_final

hora = int(input("Digite hora: "))
minutos = int(input("Digite minutos: "))
segundos = int(input("Digite segundos: "))

print(seg(hora,minutos,segundos))