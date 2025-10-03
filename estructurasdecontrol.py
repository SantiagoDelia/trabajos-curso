#--------------------------------------------------------------
# ESTRUCTURAS DE CONTROL
#--------------------------------------------------------------

# Una estructura de control en python es un bloque de codigo que permite controlar el flujo de ejecucion del programa. Estas estructuras determinan que instrucciones se ejecutaran y en que orden, basandose en condiciones especificas.

#--------------------------------------------------------------

# ESTRUCTURAS DE DECISION (CONDICIONALES):
# Permiten ejecutar cierto bloque de codigo si se cumple un condicion, de lo contrario, se ejecuta otro bloquen de codigo

# if condicion_1:
    #bloque de codigo si se cumple la condicion 1
# elif condicion_2:
    #bloque de codigo si se cumple la condicion 2
# else:
    #bloque de codigo si no se cumple ninguna condicion 

#--------------------------------------------------------------

# BUCLES (Loops):
# Permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion o hasta que se vuelva falsa 

# BUCLE WHILE:
# while condicion:
    #bloque de codigo que se ejecuta mientras la condicion sea verdadera    
# Ejemplo:  
contador = 0
while contador < 5:
    print ("El contador es:", contador)
    contador += 1

# BUCLE FOR:
# for variable in secuencia:
    #bloque de codigo que se ejecuta para cada elemento en la secuencia
# Ejemplo:
frutas = ["manzana", "banana", "cereza"]        
for fruta in frutas:
    print ("La fruta es:", fruta)           



#--------------------------------------------------------------

# ESTRTUCTURAS DE CONTROL DE EXCPECIONES: 
# Permiten manejrar errores y excpeciones en un programa, controlando como se manejan los errores cuando ocurren durante la ejecucion 

# try:
    #bloque de codigo que puede generar una excepcion

# except TipoDeExcepcion as nombre_variable:
#   #bloque de codigo que se ejecuta si ocurre la excepcion 

# finally:
    #bloque de codigo que se ejecuta siempre, haya o no excepcion
# Ejemplo:
try:
    numero = int(input("Ingresa un numero: "))
    resultado = 10 / numero
    print ("El resultado es:", resultado)
except ZeroDivisionError as e:
    print ("Error: No se puede dividir por cero.", e)
except ValueError as e:
    print ("Error: Debes ingresar un numero valido.", e)
finally:
    print ("Ejecucion del bloque finally.")
#     

#--------------------------------------------------------------

# CONDICIONALES TERNARIAS:
# las condicionales ternarias en python son una forma concisa de expresar una estructura de condicional en una sola linea
# (se utilizan principalmente para asignar valores a una variable en funcion de una condicion)
# Ej:

# variable = valor_si_verdadero if condicion else valor_si_falso

x = 4
resultado = "Es mayor que 5" if x > 5 else "No es mayor que 5"
print (resultado)

#--------------------------------------------------------------

#PALABRAS CLAVES OPARA CONTROL DE FLUJO:
# Forman parte del conjunto de herramientas que python proporciona para controlar el flujo de ejecucion de un programa. Estas palabras clave permiten definir estructuras de control como condicionales, bucles y manejo de excepciones.

# BREAK:
# Se utiliza para salir de un bucle antes de que haya terminado su ciclo completo. Cuando
# se encuentra una instruccion break dentro de un bucle, la ejecucion del bucle se detiene inmediatamente y el control del programa se transfiere a la siguiente instruccion despues del bucle.
for i in range(10):
    if i == 5:
        break
    print (i)

# CONTINUE:
# Se utiliza para saltar la iteracion actual de un bucle y pasar a la siguiente iteracion. Cuando se encuentra una instruccion continue dentro de un bucle, el resto del codigo en esa iteracion se omite y el control del programa vuelve al inicio del bucle para la siguiente iteracion.
for i in range(10):
    if i % 2 == 0:
        continue
    print (i)   

# PASS:
# Es una instruccion nula que se utiliza como un marcador de posicion en el codigo.
# Se utiliza cuando se requiere una sintaxis pero no se desea ejecutar ninguna accion.
def funcion_vacia():
    pass
# La funcion no hace nada, pero es sintacticamente correcta

#--------------------------------------------------------------

