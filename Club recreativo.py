
basico = 0
premium = 0
familiar = 0
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre == "salir":
        break
    edad = int(input("Ingrese su edad: "))
    plan = input("Ingrese su plan: ")
    if edad < 18:
        print("Muestre su registro juvenil")
    elif edad >= 60:
        print("Muestre su beneficio senor")


    if plan == "basico":
        basico1 = 50000
        basico += 1
        total3 = total3 + basico1
    elif plan == "premium":
        premium1 = 90000
        premium += 1
        total2 = total2 + premium
    elif plan == "familiar":
        familiar1 = 130000 
        familiar += 1 
        total1 = total1 + familiar


total_recaudado = total1 + total2 + total3
if basico > premium and basico > familiar:
    print("El plan mas vendido fue el basico")
elif premium > basico and premium > familiar:
    print("El plan mas vendido fue el premium")
elif familiar > basico and familiar > premium:
    print("El plan mas vendifo fu el familiar")
print(f"Cantidad de personas en premium: {premium}")
print(f"Cantidad de personas en basico: {basico}")
print(f"Cantidad de personas en familiar: {familiar}")
print(f"Total recaudado: {total_recaudado}")

