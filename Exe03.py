def posi(x):
    status = ""
    if x > 0:
        status = "Positivo. "
    elif x < 0:
        status = "Negativo."
    else:
        status = "0"

    return status

print(posi(-3))