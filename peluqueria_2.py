print("Peluqieria")
corte = 0
cepillado = 0
tintura = 0
count = 0
while count < 7:
    input("Ingrese su nombre: ")
    servicio = input("Que servicio desea: ")
    valor = float(input("Ingrese el valor: "))

    if servicio == "corte":
        corte += 1
        total = total + valor
    elif servicio == "cepillado":
        cepillado += 1
        total = total + valor
    elif servicio == "tintura":
        tintura += 1
        total = total + valor

if corte > tintura and corte > cepillado:
    print("El servicio mas solicitado fue corte")
elif tintura > corte and tintura > cepillado:
    print("El servicio mas solicitado fue tintura")
elif cepillado > corte and cepillado > tintura:
    print("El servicio mas solicitado fue cepillado")


print(f"Total del dia: {total}")
print(f"Cantida de cliente en corte: {corte}")
print(f"Cantidad de clientes en cepillado {cepillado}")
print(f"Cantidad de clientes en tintura: {tintura}")
