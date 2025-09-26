import random
import pandas as pd

from pathlib import Path

historial_juegos = []
fichas = 9
opciones_piedra_papel_tijera = ["piedra", "papel", "tijera"]

nombre = ""

def mostrar_fichas():
    print(f"Tu número de fichas es: {fichas}")

def alerta_de_fichas():
    if fichas < 10:
        print("¡Alerta! Tu cantidad de fichas es menor a 10.")
    mostrar_fichas()

def Manejo_de_fichas():
    global fichas
    while True:
        eleccion = input("¿Deseas ingresar fichas? (s/n): ").lower()
        if eleccion == "s":
            try:
                cantidad = int(input("¿Qué cantidad de fichas deseas ingresar? "))
                fichas += cantidad
                print(f"Ahora tienes {fichas} fichas.")
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif eleccion == "n":
            print(f"La cantidad actual de fichas es: {fichas}")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def piedra_papel_tijera():
    global fichas
    mostrar_fichas()
    print("\n--- Juego: Piedra, Papel o Tijera ---")

    des1 = input(f"{nombre}, elige una opción:\n"
                  "1. Piedra\n"
                  "2. Papel\n"
                  "3. Tijera\n"
                  "4. Salir\n"
                  "Tu opción es: ")

    if des1 == "4":
        print(f"Gracias por jugar, {nombre}.")
        return

    opciones_usuario = {"1": "piedra", "2": "papel", "3": "tijera"}
    if des1 not in opciones_usuario:
        print("Opción inválida. Intenta de nuevo.")
        return

    jugador = opciones_usuario[des1]
    computadora = random.choice(opciones_piedra_papel_tijera)
    print(f"Has elegido: {jugador}")
    print(f"La computadora ha elegido: {computadora}")

    if jugador == computadora:
        print("Empate.")
        resultado = "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
        fichas += 2
        resultado = "Ganaste"
    else:
        print("Perdiste.")
        fichas -= 1
        resultado = "Perdiste"

    historial_juegos.append({
        "Juego": "Piedra, Papel o Tijera",
        "Resultado": resultado,
        "Fichas": fichas
    })

def adivina_el_numero():
    global fichas
    mostrar_fichas()
    print("\n--- Juego: Adivina el número ---")
    num = random.randint(1, 10)
    intentos = 0
    max_intentos = 5

    while intentos < max_intentos:
        try:
            des1 = int(input(f"{nombre}, adivina un número entre 1 y 10 (Intento {intentos + 1}/{max_intentos}): "))
            intentos += 1
            if des1 != num:
                fichas -= 1

            if des1 < num:
                print("El número es mayor.")
            elif des1 > num:
                print("El número es menor.")
            else:
                print(f"¡Felicidades {nombre}! Adivinaste el número {num} en {intentos} intentos.")
                fichas += 1
                resultado = "Ganaste"
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
    else:
        print(f"Lo siento, {nombre}. No lograste adivinar el número. Era el {num}.")
        resultado = "Perdiste"

    historial_juegos.append({
        "Juego": "Adivina el número",
        "Resultado": resultado,
        "Fichas": fichas,
        "Intentos": intentos
    })

def dados():
    global fichas
    mostrar_fichas()
    print("\n--- Juego: Lanzamiento de dados ---")
    num_maquina = random.randint(3, 12)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    print(f"Lanzaste un {dado1} y un {dado2}. Total: {total}")
    print(f"La máquina sacó: {num_maquina}")

    if total == num_maquina:
        print(f"¡Felicidades {nombre}, has ganado!")
        fichas += 2
        resultado = "Ganaste"
    else:
        print(f"Será la próxima, {nombre}. Has perdido.")
        fichas -= 1
        resultado = "Perdiste"

    historial_juegos.append({
        "Juego": "Lanzamiento de dados",
        "Resultado": resultado,
        "Fichas": fichas
    })

def eleccion_juego():
    while True:
        alerta_de_fichas()
        try:
            des1 = int(input(f"{nombre}, selecciona un juego:\n"
                              "1-- Piedra, papel o tijera\n"
                              "2-- Adivina el número\n"
                              "3-- Dados\n"
                              "4-- Agregar fichas\n"
                              "5-- Exportar historial\n"
                              "6-- Salir\n"
                              "Tu opción es: "))
            if des1 == 1:
                piedra_papel_tijera()
            elif des1 == 2:
                adivina_el_numero()
            elif des1 == 3:
                dados()
            elif des1 == 4:
                Manejo_de_fichas()
            elif des1 == 5:
                desicion_expor = input("Si deseas exportar a Excel ingresa 1, o a JSON ingresa 2: ")
                if desicion_expor == "1":
                    importar_Excel()
                elif desicion_expor == "2":
                    importar_json()
                else:
                    print("Opción inválida.")
            elif des1 == 6:
                print(f"¡Gracias por jugar, {nombre}!")
                break
            else:
                print("Debes ingresar un número del 1 al 6.")
        except ValueError:
            print("Error: debes ingresar un número válido.")

def inicio_programa():

    global nombre
    while True:
        print("\nBienvenido al casino Teen Titans!")
        nombre = input("Por favor ingresa tu nombre: ")
        eleccion1 = input(f"¡Muy bien, {nombre}! ¿Deseas ingresar a nuestro casino? (s/n): ").lower()
        if eleccion1 == "s":
            print("¡Bienvenido!")
            eleccion_juego()
        elif eleccion1 == "n":
            print(f"¡Fue un gusto, {nombre}! Terminando operación.")
            break
        else:
            print("Por favor ingresa una de las opciones indicadas (s/n).")

def importar_Excel():

    df_historial = pd.DataFrame(historial_juegos)

    ruta_destino = Path.home()  / "historial_juegos.xlsx"
    df_historial.to_excel(ruta_destino, index=False)
    print(f"¡Historial exportado correctamente a {ruta_destino}!")

def importar_json():

    df_historial = pd.DataFrame(historial_juegos)
    
    ruta_destino = Path.home() / "historial_juegos.json"
    df_historial.to_json(ruta_destino, orient="records", indent=4)
    print(f"¡Historial exportado correctamente a {ruta_destino}!")


inicio_programa()
