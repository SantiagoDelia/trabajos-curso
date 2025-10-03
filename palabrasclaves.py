#-------------------------------------------------------------------------------
# PALABRAS CLAVE DENTRO DE LAS ESTRUCTURAS DE CONTROL: BREAK, CONTINUE, PASS
# Break: rompe el ciclo antes de que termine
# Continue: salta a la siguiente iteracion del ciclo
# Pass: no hace nada, se usa para dejar el ciclo vacio
#-------------------------------------------------------------------------------


import random

# Ej 1: Break

contador = 10
prohibido = 23
 
while contador < 25:
    print (contador)
    if contador == prohibido:
        break
    contador += 1

#---------------------------------------------------------------

# Ej 2: Continue

for i in range (10):
    if i % 2 == 0:
        continue
    print (i)

#---------------------------------------------------------------

# Ej 3: Pass3



edad = random.randint (0,25)

if edad >= 18:
    print("Podes ingresar")
elif edad == 18:
    pass
else:
    print("No podes ingresar")

 