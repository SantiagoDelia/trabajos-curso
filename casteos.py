# texto (str)

variable1= "Texto"
variable2= '12345'
variable3= "texto123"

# Numericas (int, float, complex)

variable4= 12345
variable5= 12.345
variable6= 1 + 2j

# casteo de str a int
variablecasteada= int(variable2)

# casteo de int a str
variablecasteada2= str(variable4)

# --------------------------------------------------------------


print (type(int(variablecasteada))) # <class 'str'>
print (type(variablecasteada2)) # <class 'int'>

Tupla = ("manzana", "pera", "naranja")

lista = list(Tupla)


print (type(lista)) 

# ¿como se castea? (cambiar de tipo de dato) tipoDeDato ("el dato original")    
# con type podemos saber que tipom de dato es el que estamos manejando