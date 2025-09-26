import pandas as pd
import os
from mi_rich1 import *

console = Console()

tareas = {}


def agregar_tareas():
    while True:
        print(" 📝 AGRAGAR  TAREAS")
        
        

        if input("desea agregar una tarea? (s/n) : ").lower() == "s":
            nombre_tarea = input("ingresa el nombre de la tarea: ")
            desicion = int(input("La urgencia esta dividida en 3 opciones:\n"
                                        "1--Baja\n"
                                        "2--Media\n"
                                        "3--Alta  "))
            if desicion in (1, 2, 3):

                match desicion:
                    case 1:
                        urgencia = "Baja"
                    case 2:
                        urgencia = "Media"
                    case 3:
                        urgencia = "Alta"
                tareas[nombre_tarea] = [urgencia, "  Pendiente"]
            else:
                print("debe ingresar una opcion valida")
                break
        else:
            break


def visualizar_tareas():
    print(f"sus tareas son : {tareas}")


def marcar_tareas():
    while True:
        
        print(" 📝 MARCAR  TAREAS")
        
        
        nombre = input("Ingrese el nombre exacto de la tarea que quiere marcar como realizada: ")
        if nombre in tareas:
            estado = input("Ya completo esta tarea ? (s/n): ").lower()
            if estado == "s":
                tareas[nombre][1] = "completada"
        else:
            break
        break


def eliminar_tareas():
    while True:
        print("# 📝 ELIMINAR  TAREAS")
        
        
        
        nombre = input("Ingrese el nombre exacto de la tarea que quiere eliminar: ")
        if nombre in tareas:
            estado = input("desea eliminar esta tarea? (s/n): ").lower()
            if estado == "s":
                del tareas[nombre]
        else:
            break
        break


def Exportar():
    nombres = tareas.keys()
    urgencias = [tareas[n][0] for n in nombres]
    estados = [tareas[n][1] for n in nombres]

    datos = {
        "Tarea ": nombres,
        "Urgencia ": urgencias,
        "Estado ": estados
    }
    df = pd.DataFrame(datos)
    df.to_excel("Importacion_datos.xlsx", index=False)
    print(" Ruta:", os.path.abspath("Importacion_datos.xlsx"))
    print("Exportado correctamente")


def menu():
    while True:
        seleccion = int(input(
                    "📝 Menu\n"

                    " Bien venido al menu, por favor seleccione una opcion\n"

                    "1--Agregar tarea\n"

                    "2--Visualizar tareas \n"

                    "3--Marcar tareas \n"

                   "4--Eliminar tareas    \n"

                    "5--Exportar\n"
                    
                    "6--salir\n"
                    
                    "opcion: "

                    ))

        

        if seleccion in (1, 2, 3, 4, 5, 6):
            match seleccion:
                case 1:
                    agregar_tareas()
                case 2:
                    visualizar_tareas()
                case 3:
                    marcar_tareas()
                case 4:
                    eliminar_tareas()
                case 5:
                    Exportar()
                case 6:
                    print("Terminando programa")
                    exit()


while True:
    print("📝 GESTOR DE TAREAS")
    menu()
