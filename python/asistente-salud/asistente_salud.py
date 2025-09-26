

# librerias necesarias


import os
import random
import pandas as pd

# Variables globales
imc = None
agua = None
puntaje = None
consejo_texto = None

#funciones
# Función para importar datos a un archivo Excel
def importar(nombre, peso, altura, imc, agua, puntaje_test, consejo, archivo="registro_salud.xlsx"):
    datos = {
        "Nombre": [nombre],
        "Peso (kg)": [peso],
        "Altura (m)": [altura],
        "IMC": [imc],
        "Agua recomendada (L)": [agua],
        "Puntaje Test Bienestar": [puntaje_test],
        "Consejo Saludable": [consejo]
    }

    df = pd.DataFrame(datos)
    df.to_excel(archivo, index=False)
    ruta_completa = os.path.abspath(archivo)
    print(f"\n✅ Datos guardados correctamente en:\n{ruta_completa}")
# Función para calcular el IMC
def calcular_imc():
    global imc
    print("Muy bien!. continuemos\n"
          "Calcularemos el IMC(indice de masa corporal)")

    IMC = peso / (altura**2)
    print("""
        | IMC            | Clasificación               |
        |----------------|-----------------------------|
        | Menos de 18.5  | Bajo peso                   |
        | 18.5 – 24.9    | Peso normal                 |
        | 25.0 – 29.9    | Sobrepeso                   |
        | 30.0 – 34.9    | Obesidad grado I            |
        | 35.0 – 39.9    | Obesidad grado II           |
        | 40 o más       | Obesidad grado III (mórbida)|
        """)

    match True:
        case 1 if IMC < 18.5:
            print("Su condicion es : bajo peso")
            

        case 2 if 18.5 <= IMC < 24.9:
            print("Su condicion es : Peso normal ")

        case 3 if 25.0 <= IMC < 29.9:
            print("Su condicion es : Sobrepeso")

        case 4 if 30.0 <= IMC < 34.9:
            print("Su condicion es : Obesidad grado I ")

        case 5 if 35.0 <= IMC < 39.9:
            print("Su condicion es : Obesidad grado II  ")

        case 6 if IMC >= 40.0:
            print("Su condicion es : Obesidad grado III (mórbida)")
    return IMC
# Función para generar un consejo de salud diario
def consejo():
    global consejo_texto
    consejos_salud = [
        "Incluye frutas y verduras en cada comida.",
        "Toma suficiente agua al día (al menos 2 litros o 35 ml por kg de peso).",
        "Duerme entre 7 y 9 horas cada noche.",
        "Haz al menos 30 minutos de actividad física diaria.",
        "Reduce el tiempo frente a pantallas y redes sociales.",
        "Modera el consumo de azúcares y alimentos ultraprocesados.",
        "Dedica tiempo a relajarte y manejar el estrés.",
        "Cepíllate los dientes al menos dos veces al día.",
        "Lávate las manos frecuentemente con agua y jabón.",
        "Realiza chequeos médicos preventivos una vez al año."
    ]

    consejo_diario = random.choice(consejos_salud)
    print(f"su consejo diario es : {consejo_diario}")
    return consejo_diario
# Función para calcular la cantidad de agua recomendada
def agua_diaria():
    global agua
    recomendacion_agua = peso * 0.035

    print(
        f"El dia de hoy te recomiendo beber: {recomendacion_agua:.2f} litros de agua ")
    return recomendacion_agua
# Test de bienestar
def test_bienestar():
    global puntaje

    puntaje = 0
    if input("¿Dormiste al menos 7 horas anoche?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Has tomado suficiente agua hoy?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Hiciste al menos 30 minutos de actividad física?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Comiste frutas o verduras hoy?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Te tomaste al menos 10 minutos para relajarte o desconectarte?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Pasaste menos de 2 horas en redes sociales?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Evitas alimentos ultraprocesados hoy?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Mantuviste una buena postura al sentarte/trabajar?(s/n)").lower() == "s":
        puntaje += 1

    if input(" ¿Te cepillaste los dientes al menos dos veces hoy?(s/n)").lower() == "s":
        puntaje += 1

    if input("¿Llevas hoy un buen ánimo en general?(s/n)").lower() == "s":
        puntaje += 1

    print(f"El resultado de el test fue :{puntaje}")

    if puntaje >= 8:
        print("¡Muy bien! Estás cuidando tu bienestar 👏")
        
    elif puntaje >= 5:
        print("Vas por buen camino, sigue mejorando 💪")
    else:
        print("Necesitas cuidarte más, tu salud importa ❤️")
    return puntaje
# Menu principal
def menu_principal():
    global imc, agua, puntaje, consejo_texto
    while True:
        try:
            
            
            
            eleccion = int(input("---------------------------------------------------------------------------------------------------------------------------------------------\n"
                                "---------------------------------------------------------------------------------------------------------------------------------------------\n"
                                "seleciona una opcion\n"
                                
                                "[1] Calcular IMC\n"

                                "[2] Agua recomendada\n"

                                "[3] Test de bienestar\n"

                                "[4] Consejo saludable\n"
                                
                                "[5] importar excel\n"

                                "[6] Salir\n"
                                "---------------------------------------------------------------------------------------------------------------------------------------------\n"
                                "---------------------------------------------------------------------------------------------------------------------------------------------\n"
                                ))

            if eleccion in (1, 2, 3, 4,5,6):
                print(f"Opción {eleccion} seleccionada correctamente.")
                if eleccion == 1:
                    imc = calcular_imc()

                elif eleccion == 2:
                    agua = agua_diaria()

                elif eleccion == 3:
                    puntaje = test_bienestar()

                elif eleccion == 4:
                    consejo_texto = consejo()
                    
                elif eleccion == 5:
                        
                    if None in (imc, agua, puntaje, consejo_texto):
                        print("\n❌ Debes ejecutar primero las opciones 1 a 4 para generar todos los datos antes de importar al Excel.")
                    else:
                        importar(nombre, peso, altura, imc, agua, puntaje, consejo_texto)


                elif eleccion == 6:
                    return
        except ValueError:
            print("Debes ingresar una opcion valida")

def main():
    while True:
        if input("¿Desea realizar un nuevo registro? (s/n)").lower() == "s":
            global nombre, peso, altura
            nombre = input("Ingrese su nombre: ")
            peso = float(input("Ingresa por favor tu peso: "))
            altura = float(input("Ingresa por favor tu altura en metros: "))
            menu_principal()
        else:
            print("Gracias por usar el programa.")
            break  # Salir del ciclo principal        
#codigo principal
main() 