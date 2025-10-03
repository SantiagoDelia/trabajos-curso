# ESTRUCTURAS DE CONTROL CONDICIONALES
# If, Elif, Else 
# Ej 1: 

#x = 10 


#if x > 0:
    #print ("x es un numero positivo")
#elif x < 0:
    #print ("x es un numero negativo")
#else:
    #print ("x es cero")

#--------------------------------------------------------------

# Ej 2:

# Queremos viajar internacionalmente



visa = False 
pasaporte = True

if visa and pasaporte:
    print ("Puedes viajar internacionalmente")
elif pasaporte and not visa:
    print ("Solo puedes ingresar a los paises que no requieren visa")   
else:
    print ("No puedes viajar internacionalmente")


#--------------------------------------------------------------

# Ej 3:

edad = 65


if edad <= 18 or edad >= 60:
    print ("No podes entrar a la disco")
    if edad < 18:
        print ("Eres menor de edad")
    else:
        print ("Por seguridad, no se permite el ingreso a mayores de 60 años")
elif edad > 18 and edad < 60:
    print ("Podes entrar a la disco")


#--------------------------------------------------------------

