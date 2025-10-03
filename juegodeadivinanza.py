import random


numero_secreto = random.randint(1, 101)
intentos = 0
maximoIntentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinanza!")
while not adivinado:
    if not intentos < maximoIntentos:
       print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.") 
       break


    numero = int(input("Adivina un número entre 1 y 100: " ) )
    
    if numero == numero_secreto:
        print("¡Felicidades! ¡Has adivinado el número!") 
        adivinado = True
    elif numero < numero_secreto:
        print(f"El número es más alto. Intenta de nuevo. Te quedan {maximoIntentos - intentos - 1} intentos.")
    else:
        print(f"El número es más bajo. Intenta de nuevo. Te quedan {maximoIntentos - intentos - 1} intentos.")

    intentos += 1

