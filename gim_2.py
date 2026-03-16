print("Mida su promedio ")
low_commitment = 0
high_commitment = 0
moderate_commitment = 0
totale = 0
count = 0

while count < 3:

    name = input("Ingrese su nombre: ")
    days = int(input("Cuantos dias asisto en la semana: "))
    int(input("Cuantos minutos entrena por dia: "))

    if days < 3:
        low_commitment = low_commitment + 1
        count = count + 1
        totale = totale + 1
        print(f"Bajo compromiso, {name}")
    elif 3 <= days and days <= 4:
        moderate_commitment = moderate_commitment + 1 
        count = count + 1
        totale = totale + 1
        print(f"Compromiso medio, {name}")
    elif days >= 5:
        high_commitment =  high_commitment + 1
        count = count + 1
        totale = totale + 1
        print(f"Altos compromiso alto, {name}")



print(f"Total de bajo compromiso: {low_commitment}")  
print(f"Total de compromiso moderado: {moderate_commitment}") 
print(f"Total de alto compromiso {high_commitment}")     
print(f"Total de registros {totale}")
