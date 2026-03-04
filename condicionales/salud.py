edad = int(input("Digite su edad: "))

if edad >= 0 and edad <=120:
    if edad < 6:
        etapa = "infancia"
    elif edad < 12:
        etapa = "Niñez" 
    elif edad < 20:
        etapa = "Adolescencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = " Adultez"
    else:
        etapa = "Vejez"
    print (f"La etapa que estas viviendo es {etapa}")
else: 
    print ("La edad introducida no es valida")