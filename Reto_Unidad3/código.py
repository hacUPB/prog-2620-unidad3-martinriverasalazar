# Consumo base del avión (kg/km)
consumo_base = 6
 
# Combustible inicial
combustible = 158790
 
# Reserva mínima
reserva_minima = 10000
 
# Número de tramos
tramos = int(input("Ingrese el número de tramos del vuelo: "))
 
for i in range(tramos):
 
    print("\nTramo", i+1)
 
    distancia = float(input("Ingrese la distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind / tailwind / crosswind): ")
 
    consumo = consumo_base
 
    if viento == "headwind":
        consumo = consumo_base * 1.18
    elif viento == "tailwind":
        consumo = consumo_base * 0.88
    elif viento == "crosswind":
        consumo = consumo_base
 
    consumo_tramo = distancia * consumo
 
    # Verificación antes de consumir
    if combustible - consumo_tramo < reserva_minima:
        print("ALERTA CRÍTICA")
        print("Combustible insuficiente para continuar.")
        print("Desviando al aeropuerto alterno.")
        break
 
    combustible -= consumo_tramo
 
    print("Combustible restante:", combustible, "kg")
 
print("Fin de la simulación")