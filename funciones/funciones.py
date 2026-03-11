# crear una funcion qué calcule el factorial de un número 


def factorial(numero):
    # Si numero es 0 el factorial es 1
    # Si numero es menor que cero retornar no existe 
    if numero < 0:
        return "error"
    else:
    # multiplicar desde 1 hasta número y acumular el resultado 
        acumulador = 1
        for factor in range(1,numero+1):
            acumulador = acumulador * factor
         #acumulador *= factor 
    return acumulador 

resultado = factorial (4)
print (resultado)
