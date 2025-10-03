nombre1 = input("Hola jugador 1, como te llamas? ")
nombre2 = input("Hola jugador 2, como te llamas? ")

jugador1 = input("Hola," + nombre1 + ",que elegis? piedra, papel o tijera:" )
jugador2 = input("Hola," + nombre2 + "que elegis? piedra, papel o tijera: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "tijera" and jugador2 == "papel"
condicion3 = jugador1 == "papel" and jugador2 == "piedra"

turno = 0
maximoTurnos = 5

while turno < maximoTurnos:
    turno += 1
    print("Turno", turno)
    jugador1 = input("Hola," + nombre1 + ",que elegis? piedra, papel o tijera:" )
    jugador2 = input("Hola," + nombre2 + "que elegis? piedra, papel o tijera: ")
    if turno == maximoTurnos:
        print("Se acabaron los turnos")
        break

if jugador1 == jugador2:
    print("Empate!")    
elif condicion1 or condicion2 or condicion3:
    print("Gana ", nombre1)
else:
    print("Gana", nombre2)
    
    
    

