# Función menú: imprime un menú de opciones y retorna la opción elegida por el usuario.

def menu():
    # No se debe permitir seleccionar una opción que no está en el menú
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")01
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print ("Opción elegida no válida ...\n")
    return opcion

operación = menu()
print (f"El usuario eligió la opción {operación}")