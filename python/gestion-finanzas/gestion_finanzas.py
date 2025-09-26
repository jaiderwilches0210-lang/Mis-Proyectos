
import pandas as pd
from mi_rich1 import *
import os
import json
salario = None
fecha_salario = None
contador = iter(range(0,10000))
saldo = 10000
movimientos_bancarios = {}
Alimentación = {}
Transporte = {}
servicios = {}
Ocio = {}
Otros = {}
gastos={}
presupuesto = 0
cobros_mensuales =[]
clave = "Programador"
usuario = "Jaider"

def guardar_datos():
    with open ("movimientos.json", "w", encoding= "utf-8") as f:
        json.dump(movimientos_bancarios,f,indent=4, ensure_ascii= False)

def ingreso_mensual():
    global fecha_salario, numero
    
    hoy = datetime.now()
    mes = hoy.month+1
    año = hoy.year  
    if mes > 12:
        mes = 1
        año += 1
    fecha_salario = f"{int(dia):02}/{mes:02}/{año}"
    
    if fecha_salario == fecha_actual:
        
        numero = next(contador)
        movimientos_bancarios[numero] = {
                    "Fecha": fecha_formateada,
                    "Valor": int(salario),
                    "Descripcion": "Salario",
                    "Categoria": "otros"
                }
        manejo_del_saldo(numero)
        movimientos_bancarios[numero]["Saldo"] = saldo
         
def asignacion_ingreso_mensual():
    
    global salario, fecha_salario, dia
    
    salario = input("porfavor ingresa el valor del salario  que recibes mensualmente: ")
    dia = input("Por favor ingresa el dia aporximado que te consignan este dinero: ")
    
    hoy = datetime.now()
    mes = hoy.month
    año = hoy.year
    
    fecha = f"{int(dia):02}/{mes:02}/{año}"
    print(f"la fecha asignada es: {fecha}")
    print(f"El salario registrado es: {salario}")
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"salario": salario, "dia": dia}, f)
    
def verificar_primera_vez():
    global movimientos_bancarios,salario,dia
    
    if not os.path.exists("registro_ingreso.txt"):
        with open("registro_ingreso.txt", "w") as f:
            f.write("ejecutado")
        asignacion_ingreso_mensual()  
        menu()
        
    else:
        print("Ya registraste tu ingreso mensual.")
        
        if os.path.exists("movimientos.json"):
            with open("movimientos.json", "r", encoding='utf-8') as f:
                movimientos_bancarios = json.load(f)
                movimientos_bancarios = {int(k): v for k, v in movimientos_bancarios.items()}
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="utf-8") as f:
                config = json.load(f)
                salario = config.get("salario")
                dia = config.get("dia")      
        if os.path.exists("cobros_mensuales.json"):
            with open("cobros_mensuales.json", "r", encoding="utf-8") as f:
                cobros_mensuales = json.load(f) 
                         
        else:
            movimientos_bancarios = {}


        menu()

def manejo_del_saldo(numero):
    global saldo
    
    saldo_actual = saldo 
    nuevo_saldo = movimientos_bancarios[numero]["Valor"] + saldo_actual
    saldo = nuevo_saldo

def registro_movimientos():   
    global numero
    while True:
        guardar_datos()
        des = input("Desea ingresar un nuevo registro o movimiento bancario?(s/n): ").lower()
        
        if des in ["s", "n"]:
            
            if des == "s":
                
                numero = next(contador)
                valor = int(input("Ingrese el valor del movimiento: "))
                descripcion = input("Por favor ingrese la descripcion del movimiento  : ")
                categoria = input("agrupelo en una de estas categorias :Alimentación, Transporte, Servicios, Ocio, Otros : ").lower()
                
                movimientos_bancarios[numero] = {
                    "Fecha": fecha_formateada,
                    "Valor": valor,
                    "Descripcion": descripcion,
                    "Categoria": categoria
                }
                manejo_del_saldo(numero)
                movimientos_bancarios[numero]["Saldo"] = saldo
                
            elif des == "n":
                break
        else:
            print("Por favor ingrese una opcion valida")

def filtrado():
    
    des2 = int(input("1--Filtrar por fecha\n"
                     "2--Filtrar por tipo de movimiento\n"))
    
    if des2 in [1, 2]:
    
        if des2 == 1:
            
            filtro = input("Que fecha desea buscar? por favor ingresela en formato (DD/MM/AAAA)")
            for movimiento in movimientos_bancarios.values():
                if movimiento["Fecha"] == filtro:
                    print(movimiento)
        elif des2 == 2:
            
            filtro = int(input("1--Filtrar por ingresos\n"
                               "2--Filtrar por salidas\n"))
            
            if des2 in [1, 2]:
                       
                if filtro == 1:
                    for movimiento in movimientos_bancarios.values():
                        if movimiento["Valor"] > 0:
                            print(movimiento)
                elif filtro == 2:    
                    for movimiento in movimientos_bancarios.values():
                        if movimiento["Valor"] < 0:
                            print(movimiento)
            else:
                print("Por favor ingrese una opcion valida")
    else:
        print("Por favor ingrese una opcion valida")

def categorias():
    for numero, datos in movimientos_bancarios.items():
        categoria = datos["Categoria"]
        match categoria:
            case "alimentacion":
                Alimentación[numero] = datos
            case "transporte":
                Transporte[numero] = datos
            case "servicios":
                servicios[numero] = datos
            case "ocio":
                Ocio[numero] = datos
            case "otros":
                Otros[numero] = datos

def menu():
    while True:
        ingreso_mensual()
        modificar_presupuesto()
        presupuesto_alerta()
        Manejo_gastos() 
        categorias()
        
        des3 = int(input("1--Registro de movimientos\n"
                         "2--Filtrado\n"
                         "3--Visualizar por categoria\n"
                         "4--Vsualizar el mayor gasto\n"
                         "5--Visualizar movimientos\n"
                         "6-- Exportar\n"
                         "7--Salir\n"))
        
        if des3 in [1,2,3,4,5,6,7]:
            if des3 == 1:
                registro_movimientos()
            elif des3 == 2:
                filtrado()
                         
            elif des3 == 3:
                print(f"Alimentación: {Alimentación}")
                print(f"Transporte: {Transporte}")
                print(f"servicios: {servicios}")
                print(f"Ocio: {Ocio}" )
                print(f"Otros: {Otros}" )             
                
            elif des3 == 4:
                mayor_gasto()
            elif des3 == 5:
                print(movimientos_bancarios)    
            elif des3==6:
                exportacion() 
            elif des3==7:
                guardar_datos
                exit()     
                        
        else:
            print("Ingrese una opcion valida por favor")

def mayor_gasto():
    global gastos
    maximo = 0
    for movimiento in movimientos_bancarios:  
        if movimientos_bancarios[movimiento]["Valor"] < 0:
            if abs(movimientos_bancarios[movimiento]["Valor"]) > maximo:
                maximo = abs(movimientos_bancarios[movimiento]["Valor"])
                gastos = movimientos_bancarios[movimiento]
                
    print(f"\nGasto más alto del mes:\n"
          f"Valor: ${maximo}\n"
          f"Descripción: {gastos['Descripcion']}\n"
          f"Fecha: {gastos['Fecha']}\n"
          f"Categoría: {gastos['Categoria']}")  

def exportacion():
    
    try:
        df = pd.DataFrame.from_dict(movimientos_bancarios, orient="index")
        df.to_excel("informe_movimientos.xlsx", index=False)
        print("✅ Exportación exitosa.")
    except PermissionError:
        print("❌ Error: Cierra el archivo 'informe_movimientos.xlsx' antes de exportar.")

def modificar_presupuesto():
    global presupuesto, fecha_limite

    hoy = datetime.now().strftime("%d/%m/%Y")

    if os.path.exists("presupuesto.json"):
        with open("presupuesto.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
            presupuesto = datos.get("presupuesto", 0)
            fecha_limite = datos.get("fecha_limite", "01/01/1900")

        
        if hoy >= fecha_limite:
            print("⏰ Ha pasado la fecha límite del presupuesto.")
            presupuesto = int(input("Ingrese el nuevo presupuesto mensual: "))
            fecha_limite = input("Nueva fecha límite (DD/MM/AAAA): ")
            with open("presupuesto.json", "w", encoding="utf-8") as f:
                json.dump({
                    "presupuesto": presupuesto,
                    "fecha_limite": fecha_limite
                }, f)
    else:
        
        presupuesto = int(input("Ingrese su presupuesto mensual: "))
        fecha_limite = input("Fecha límite (DD/MM/AAAA): ")
        with open("presupuesto.json", "w", encoding="utf-8") as f:
            json.dump({
                "presupuesto": presupuesto,
                "fecha_limite": fecha_limite
            }, f)

def presupuesto_alerta():
    if saldo < presupuesto:
        print("⚠️ ALERTA: Ha sobrepasado su presupuesto")
    else:
        print("✅ Todo bajo control. Aún estás dentro del presupuesto.")

def Gastos_mensuales():
    global cobros_mensuales
    while True:
        des4 = input("¿Desea agregar un gasto mensual? (s/n): ").lower()
        if des4 == "s":
            nombre_gasto = input("Ingrese el nombre del gasto: ")
            valor_mensual = int(input("Ingrese el valor del gasto: "))
            dia_vencimiento = int(input("Ingrese el día que se vence la factura: "))

            hoy = datetime.now()
            mes = hoy.month + 1
            año = hoy.year

            if mes > 12:
                mes = 1
                año += 1

            fecha_cobro = f"{dia_vencimiento:02}/{mes:02}/{año}"
            cobros ={"Nombre": nombre_gasto, "Fecha": fecha_cobro , "Valor" :valor_mensual*-1 }
            cobros_mensuales.append(cobros)
            
            print(f"🔁 Gasto recurrente '{nombre_gasto}' programado para el {fecha_cobro} por ${valor_mensual}")
            # Aquí puedes guardar en una estructura si quieres
        elif des4 == "n":
            break
        else:
            print("Por favor ingrese una opción válida (s/n).")
            
    with open("cobros_mensuales.json", "w", encoding="utf-8") as f:
        json.dump(cobros_mensuales, f, indent=4, ensure_ascii=False)
        
def Manejo_gastos():
    for movimiento in cobros_mensuales:
        if movimiento["Fecha"] == fecha_actual:
            numero = next(contador)
            movimientos_bancarios[numero]={
                "Fecha": movimiento["Fecha"],
                "Valor": movimiento["Valor"],
                "Descripcion": movimiento["Nombre"],
                "Categoria": "servicios"  
                
            }
            manejo_del_saldo(numero)
            movimientos_bancarios[numero]["saldo"] = saldo
            print(f"💸 Gasto mensual '{movimiento['Nombre']}' registrado automáticamente.")

def login():
    while True:
        usuario_ingresado = input("Por favor ingrese el nombre de usuario : ")
        if usuario_ingresado == usuario:
            
            clave_ingresada = input("Por favor ingrese la clave : ")
            if clave_ingresada == clave:
                verificar_primera_vez()
            else:
                print("Clave incorrecta")
                continue
        else:
            print("Ingrese un usuario registrado")    
login()
# Mostrar gráficos de barras o pastel por categoría














