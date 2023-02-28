import random

def jugar():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1
        if intento == numero_aleatorio:
            print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
            jugar_de_nuevo()
            break
        elif intento < numero_aleatorio:
            print("El número es mayor.")
        else:
            print("El número es menor.")

def jugar_de_nuevo():
    respuesta = input("¿Quieres jugar de nuevo? (s/n) ")
    if respuesta == "s":
        jugar()

print("Bienvenido al juego de adivinanza de números.")
jugar()
