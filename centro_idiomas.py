estudiantes = []

total_promedios = 0
promedio_max = -1
best = ""
bajo = 0
medio = 0
alto = 0



while True:
    nombre = input("Ingrese su nombre: (Esbriba salir y desea salir )")
    if nombre == "salir":
        break

    speaking = float(input("Ingrese su nota speaking: "))
    reading = float(input("Ingrese su nota reading: "))
    listening = float(input("Ingrese su nota de listening: "))

    promedio = (reading + speaking + listening) / 3


    if promedio < 60:
        print(f"Promedio bajo {nombre}")
        bajo += 1
    elif 60 <= promedio <= 79:
        print(f"Promedio medio {nombre}")
        medio += 1
    else: 
        print(f"Promedio alto {nombre}")
        alto += 1


   
    total_promedios += promedio
    estudiantes.append(nombre)

    if promedio > promedio_max:
        promedio_max = promedio
        best = nombre 
            

if estudiantes:
    promedio_general = total_promedios / len(estudiantes)
    print("Resumen")
    print(f"Promedio general {total_promedios}")
    print(f"Mejor estudiante: {best} su promedio fue de: {promedio_max}")
    print(f"Cuantos quedaron en bajo {bajo}")
    print(f"Cuantos quedaron en medio {medio}")
    print(f"Cuantos quedaron en alto {alto}")



    
