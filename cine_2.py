print("Control de sala de cine")
capacity = 0
child = 0
adult = 0
adult_max = 0
total = 0
capacity_max = int(input("Ingresa la capacidad maxima del cine: "))

while capacity < capacity_max:
        year = input("Ingrese su edad: ")
        if year == "salir":
            break
        
        if year < "9":
            child = child + 1
            capacity = capacity + 1
            total = total + 1
        elif "9" <= year and year <= "59":
            adult = adult + 1
            capacity = capacity + 1
            total = total + 1
        elif year >= "60":
            adult_max = adult_max + 1
            capacity = capacity + 1
            total = total + 1
        
        if capacity == capacity_max:
            t = "Si"
        else:
            t = "No"

        
   




print(f"Total de personas ingresadas: {total}")     
print(f"Cuantos niños ingresaron: {child}")  
print(f"Cuantos adultos ingresaron: {adult}")
print(f"Cuantos adultos mayores ingresaron {adult_max}")
print(f"La sala esta llena: {t}")


