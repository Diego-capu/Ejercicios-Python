print("Cafeteria")
print("Menu")
print("Cafe = 4000, Capuchino = 7000, Pastel = 6000")
total1 = 0
while True:
    print("Si no desea realizar un pedido presione (1)")
    product = input("Ingrese el producto que desea: ")
    amount = int(input("Ingrese la cantidad: "))
    if product == "1":
        break
    if product == "cafe":
        coffe = 4000
        total = coffe * amount 
        print(f"Total: {total}")
        if total >= 20000:
            discont = total * 0.10
            total_discont = total - discont
            print(f"Total con descuento {total_discont}")
    elif product == "capuchino":
        capuchino = 7000
        total = capuchino * amount 
        print(f"Total: {total}") 
        if total >= 20000:
            discont = total * 0.10
            total_discont = total - discont
            print(f"Total con descuento {total_discont}")  
    elif product == "pastel":
        cake = 6000
        total = cake * amount
        print(f"Total {total}") 
        if total >= 20000:
            discont = total * 0.10
            total_discont = total - discont
            print(f"Total con descuento {total_discont}")  
            
        

print(f"Total del dia {total1}")
 
