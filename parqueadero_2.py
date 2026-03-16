print("Parqueadero")

count = 0
carros = 0
motos = 0



while count < 8:
        
        placa = input("Ingrese su placa: ")
        tipo = input("Ingrese su tipo: ")
        horas = int(input("Ingrese sus horas: "))



        if tipo == "carro":
            carro = 4000
            total1 = carro * horas
            carros += 1
        elif tipo == "moto":
            moto = 2000
            total2 = moto * horas
            motos += 1

totale = total1 + total2  
if total1 > total2:
     print("El vehiculo que pago mas el carro")
else:
     print("El vehiculo que pago mas fue la moto")
          

print(f"Total recaudado {totale}")   
print(f"Cuantos carros ingresaron:{carros}") 
print(f"Cuantas motos ingresaron: {motos}")
        

