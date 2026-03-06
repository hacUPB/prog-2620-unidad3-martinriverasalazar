articulo1 = int(input("Ingrese el valor del articulo 1: "))
articulo2 = int(input("Ingrese el valor del articulo 2: "))
articulo3 = int(input("Ingrese el valor del  articulo 3: "))

total = articulo3 + articulo1 + articulo2

if articulo1 < articulo2:
    temp = articulo1
else: 
    temp = articulo2

if temp < articulo3:
    menor = temp
else: 
    menor = articulo3

total = total - (menor * 0.5)

print (f"El total es $ {total}")