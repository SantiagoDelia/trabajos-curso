#-------------------------------------------------------------------------------
# BUCLE DE MANEJO DE ERRORES: TRY, EXCEPT, FINALLY
# manejo de la division por cero 
#-------------------------------------------------------------------------------    

import random


a = 10 
b = random.randint(0,2)
try: 
    resultado = a/b
    print (resultado)
except ZeroDivisionError:
    print ("No se puede dividir por cero")
finally: 
    if b == 0:
        print ("El valor de b es cero, no se puede dividir")
    else:
        print ("El valor de b es distinto de cero, se puede dividir")

#-------------------------------------------------------------------------------
# PALABRAS CLAVES EN ESTRUCTURAS DE CONTROL: BREAK, CONTINUE, PASS
# Break: rompe el ciclo antes de que termine
# Continue: salta a la siguiente iteracion del ciclo        
# Pass: no hace nada, se usa para dejar el ciclo vacio
#-------------------------------------------------------------------------------

# Ej 1: Break
contador = 10
prohibido = 23 
while contador < 25:
    print (contador)
    if contador == prohibido:
        break
    contador += 1
print ("Fin del ciclo")
#--------------------------------------------------------------
