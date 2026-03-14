print("Hora de llegada")
while True:
    hora = int(input("-"))
    if 6 <= hora and hora < 11:
        print("Horario de llegada (Mañana)")
    elif 12 <= hora and hora < 17:
        print("Horario de llegada (Tarde)")
    elif 18 <= hora and hora < 22:
        print("Horario de llegada (Noche)")
    else:
        print("Fuera de horario")
