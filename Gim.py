
while True: 
    edad = int(input("Ingresa tu edad: "))
    if edad < 13:
        print("No puede ingresar")
    elif 13 <= edad and edad < 17:
        print("Clase juvenil")
    elif 18 <= edad and edad < 59:
        print("Clase general")
    elif edad >60:
        print("Clase senior")
