print("Parquedero")
print("Cuantas horas estuvo en el parqueadero")
hora = int(input("-")) 
primera_hora = 5000
adicional = 3000

if hora == 1:
    total = primera_hora
    print(f"total a pagar {total}")
elif hora == 2:
    total = primera_hora + adicional 
    print(f"total a pagar {total}")
elif hora >= 3:
    total = primera_hora + adicional * hora 
    print(f"Total a pagar {total}")
