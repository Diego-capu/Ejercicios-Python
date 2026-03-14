
sabor1 = "fresa"
sabor2 = "chocolate"
sabor3 = "vainilla"


while True:
    print("Lista de helados: fresa, chocolate, vainilla")
    

    if input("Escriba el helado que desea: ") == "fresa":

        fresa = sabor1 + 1
    elif input("Escriba el helado que desea: ") == "vainilla":
        
        vainilla = sabor2 + 1
    elif input("Escriba el helado que desea: ") == "chocolate":

        chocolate = sabor3 + 1

    print(f"Helados sabor fresa {fresa}")
    print(f"Helados sabor fresa {vainilla}")
    print(f"Helados sabor fresa {chocolate}")
