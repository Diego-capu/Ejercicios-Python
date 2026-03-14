print("Elija su servicio")
while True: 
    service = input("-")

    if service == "masaje" or "MASAJE" or "Masaje":
        print("El servicio existe")
    elif service == "facial" or "FACIAL" or "Facial":
        print("El servicio existe")
    elif service == "manicure" or "MANICURE" or "Manicure":
        print("El servicio existe")
    else:
        print("Este servicio no existe")
