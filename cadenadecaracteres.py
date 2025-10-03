#cadena de caracteres, entonces, podemos trabajar con sus caracteres? Si
#el indice empieza en 0 porque indica el lugar o posicion donde esta un elemento en una estrucrtura o grupo de datos

txt = """ESTE TEXTO ESTA EN MAYUSCULAS"""


#print("ESTE" in txt) 

#print(txt [5:]) #imprime los primeros 5 caracteres


#minusculas = txt.lower() #convierte todo a minusculas
#print(minusculas)

#--------------------------------------------------------------

txt1 = """este texto esta en minusculas"""
#mayusculas = txt1.upper() #convierte todo a mayusculas
#print(mayusculas)

#--------------------------------------------------------------



txt2 = "               Hola! Hay mucho espacio en blanco aca D:"

#txtcorregido = txt2.strip() #elimina los espacios en blanco al inicio y al final
#print(txtcorregido)

#--------------------------------------------------------------

a = "Hola"
b = "Mundo"
c = a + " " + b #concatena las dos cadenas de caracteres

print(c)

#--------------------------------------------------------------

txt3 = "El contenido de este curso me esta gustando mucho y va a durar: {} horas, con un total de {} clases"

horas = 3

clases = 12

#concatenado = txt3 + str(horas) #convierte el numero a cadena de caracteres para poder concatenarlo

#print (txt3.format(horas, clases)) #forma mas facil de concatenar cadenas de caracteres y variables

#--------------------------------------------------------------

#\n salto de linea
#\t tabulador
#\b espacio en blanco



txt4 = "me gusta mucho comer \"pan\"" #el \ antes de las comillas dobles sirve para que no se cierren las comillas dobles del inicio

#print(txt4)

#--------------------------------------------------------------

