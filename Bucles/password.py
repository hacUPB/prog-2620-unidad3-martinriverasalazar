password = "pabloeshermoso"

texto = ""
contador = 1

while password != texto:
    texto = input("Ingrese la contraseña: ")
    if password != texto:
        print ("Contraseña invalida")
    print (contador)
    contador += 1

print ("Acceso Denegado")