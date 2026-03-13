# La moneda en pesos colombianos
compra = int(input("Ingrese el valor de la compra: "))
# total = compra + 9000
# if compra > 100000:
#   total = compra
envio = 0
if compra < 100000:
    envio = 9000
total = compra + envio

print (f"El valor a pagar es de ${total}")
