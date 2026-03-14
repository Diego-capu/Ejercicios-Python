print("Tienda deportiva")
print("Ingrese el precio de sus productos")
limit = 0
total = 0
while limit < 6:

    producto = float(input("-"))

    if producto >= 100000:

        total = total + 1

        limit = limit + 1 
        print("Registro exitoso")
    else:
        print("Registro exitoso")
        limit = limit + 1 
