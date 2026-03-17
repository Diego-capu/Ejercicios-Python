agotado = 0
bajo = 0
normal = 0
count = 0
while count <= 10 :
    producto = ("Ingrese el producto: ")
    cantidad = ("Ingrese la cantidad: ")


    if cantidad == 0:
        agotado += 1
        count += 1
    elif 1 >= cantidad >= 5:
        bajo += 1
        count += 1
    else:
        normal += 1
        count += 1

print(f"Stock agotado {agotado}")
print(f"Stock bajo {bajo}")
print(f"Stock {normal}")       
