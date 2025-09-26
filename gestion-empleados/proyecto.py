import statistics
#usuarios
Administradores = {"jaider":{"clave":"123"},
                   "laura":{"clave":"456"},
                   
                   "adriana":{"clave":"789"},
                   "jairo":{"clave":"1098"},
                   "samantha":{"clave":"765"}
                   }
Empleados = {
            "juan": {"clave": "123"},
            "alberto": {"clave": "123"},
            "cristian": {"clave": "123"}
            }

salarios = {x:{"salario":1423500} for x in Empleados }
#Variable global para la funcion login()
intentos = 0
#inicio de sesion  
def login():
    """
    Inicio de sesion y valida el tipo de usuario
    
    Esta funcion solicita el usuario y la contraseña datos con los cuales se hace una validacion para verificar siesun empleado
    o un administrador. Si todos los datos son correctos ejecuta a la funcion Menu().La Funcion cuenta con un manejo de errores
    en caso de no econtrar el usuario o de que la clave este incorrecta
    
    Variables globales utilizadas:
        Administradores (dict): Diccionario anidado que contiene usuarios administradores y sus claves.
        empleados (dict): Diccionario anidado que contiene usuarios empleados y sus claves.
        intentos (int): Contador global de intentos fallidos de inicio de sesión.
   
    Manejo de errores:
        Si el usuario no existe, muestra un mensaje de "usuario no encontrado".
        Si la contraseña es incorrecta, permite hasta 3 intentos antes de bloquear el acceso.
    
    Flujo:
        1. Solicita nombre de usuario.
        2. Verifica si el usuario existe en Administradores o Empleados.
        3. Solicita la contraseña y valida.
        4. Si es correcta, muestra mensajes de bienvenida e inicia `Menu()`.
        5. Si la contraseña es incorrecta más de 3 veces, bloquea el acceso.
        6. Si el usuario no existe, muestra mensaje de error y solicita nuevamente.

    Retorna:
        None: La función maneja la navegación interna y mensajes; no retorna valores.    
        
    """
    while True:
        global intentos
        usuario_ingresado = input("Ingrese el usuario:")
        if usuario_ingresado in Administradores:
            print(f"Bienvenido Admin {usuario_ingresado}")
            while True:
                clave_ingresada = input("Ingrese la clave:")
                if clave_ingresada == Administradores[usuario_ingresado]["clave"]:
                    print("ingresando...")
                    print("inicio exitoso")
                    Menu_Administrador()
                else:
                    intentos +=1
                    if intentos>3:
                        break
                
        elif usuario_ingresado in Empleados:
            print(f"Bienvenido {usuario_ingresado}")
            while True:
                clave_ingresada = input("Ingrese la clave:")
                if clave_ingresada == Empleados[usuario_ingresado]["clave"]:
                    print("ingresando...")
                    print("inicio exitoso")
                    Menu_Empleado()
                else:
                    intentos +=1
                    if intentos>3:
                        break
            
        else:
            print("usuario no encontrado")        
#Menu para los usuarios tipo Administradores        
def Menu_Administrador():
    """
    Menu de opciones
    
    La funcion da a elegir al usuario una opcion de 5 (1--Agregar empleado-2-Eliminar empleado 3--Mostrar lista de empleados
    4--Mostrar estadísticas 5--Salir"), cuenta con un manejo de errores en caso de que no se seleccion una opcion valida
    
    Manejo de errores:
        Si la opcion ingresada no esta en [1,2,3,4,5] muestra un error y pide al usuario nuevamente
        
    Flujo de ejecicion:    
        1. Muestra el menú con opciones numeradas:
                1--Agregar empleado
                2--Eliminar empleado
                3--Mostrar lista de empleados
                4--Mostrar estadísticas
                5--Salir
            2. Solicita al usuario que ingrese una opción.
            3. Valida que la opción sea un número entre 1 y 5.
            4. Según la opción seleccionada:
                a. 1: Llama a `Agregar_empleado()`.
                b. 2: Llama a `Eliminar_empleado()`.
                c. 3: Llama a `Mostrar_empleados()`.
                d. 4: Llama a `Mostrar_Estadisticas()`.
                e. 5: Sale del menú y finaliza la función.
            5. Si se ingresa un valor no numérico o fuera de rango, muestra un mensaje de error y solicita de nuevo la opción.

        
    Retorna:
        None: La función maneja la navegación interna y mensajes; no retorna valores.       
    """
    while True:
        opcion = int(input("========Menu Administrador========\n"
                        "1--Agregar empleado\n"
                        "2--Eliminar empleado\n"
                        "3--Mostrar lista de empleados\n"
                        "4--Mostrar estadísticas\n"
                        "5--Salir\n"
                        "Opcion: "))
        
        if opcion not in [1,2,3,4,5]:
            print("Ingrese una opcion valida")
        else:
            match opcion:
                case 1:    
                    print("Opcion seleccionada correctamente")
                    Agregar_empleado()
                case 2:    
                    print("Opcion seleccionada correctamente")
                    Eliminar_empleado()
                    
                case 3:    
                    print("Opcion seleccionada correctamente")
                    Mostrar_Usuarios()
                case 4:    
                    print("Opcion seleccionada correctamente")
                    Mostrar_Estadisticas()
                case 5:  
                    print("Opcion seleccionada correctamente")
                    print("Saliendo")
                    exit()  
#Menu para los usuarios tipo Empleado        
def Menu_Empleado():
    """
    Muestra el menú principal para empleados y permite consultar información.

    Flujo:
        1. Muestra el menú con opciones numeradas:
            1--Ver mis datos
            2--Consultar estadísticas generales
            3--Salir
        2. Solicita al usuario que ingrese una opción.
        3. Valida que la opción sea un número entre 1 y 3.
        4. Según la opción seleccionada, ejecuta la acción correspondiente.
        5. Si se ingresa un valor no numérico o fuera de rango, muestra un mensaje de error y solicita de nuevo la opción.
    """
    while True:
            opcion = int(input(
                                "========Menu Empleado========\n"
                                "1--Ver mis datos\n"
                                "2--Consultar estadísticas generales\n"
                                "3--Salir\n"
                                "Opción: "
                                ))
            if opcion not in [1, 2, 3]:
                print("Ingrese una opción válida")
            else:
                match opcion:
                    case 1:
                        pass
                    case 2:
                        print("Mostrando estadísticas individuales...")
                        Mostrar_Estadisticas_empleado()
                    case 3:
                        print("Saliendo del menú...")
                        break
#Funcion para agregar un nuevo empleado
def Agregar_empleado():
    """
    Funcion que agrega un nuevo usuario a uno delos diccionarios
    
    la funcion pregunta si se desea agregar un empeleado. en caso de la respuesta ser "s" se hara una verficacion y depues pedira los 
    datos del empleado como el nombre y el rol. el rol lo pide con 2 opciones, 1 y 2 las cuales son correspondientes a empleado y admnustrador
    luego pide la clave y la agrega al diccionario.
    
    Variables globales utilizadas:
        Administradores (dict): Diccionario anidado que contiene usuarios administradores y sus claves.
        empleados (dict): Diccionario anidado que contiene usuarios empleados y sus claves.
    
    Manejo de Errores:
        La funcion cuenta con varios manejosde errores para que se ingrese alguno de los datos requeridos. de no ser asi mostrara un error y lo solicitara de nuevo
    
    Flujo:
        1. Pregunta si se desea agregar un empleado:
        2. Valida que la opción sea una de las requeridas.
            -de ser la respuesta "s":
                -solicitara le nombre del empleado
                -solicitara el rol:
                    -Según la opción seleccionada, ejecuta la acción correspondiente.
                    -solicitara la clave        
        3. Si se ingresa un valor no numérico o fuera de rango, muestra un mensaje de error y solicita de nuevo la opción.
    """
    while True:
        confirmar_continuidad= input("Desea agregar un empleado?(s/n): ").lower()
        if confirmar_continuidad in ["s","n"]:
            if confirmar_continuidad == "s":
                nombre = input("ingrese el nombre del nuevo empleado: ")
                rol_m = input("si es empleado escriba 1 si es admin esrcriba 2: ")
                if rol_m in["1","2"]:
                    if rol_m == "1":
                        Empleados[nombre] = {"clave":input("ingrese la clave del nuevo usuario: ")}
                        print("nuevo usuario creado")
                        
                    else:
                        Administradores[nombre] = {"clave":input("ingrese la clave del nuevo usuario: ")}
                        print("nuevo usuario creado")
                else:
                    print("ingrese una opcion valida")        
            else:
                print("saliendo...")       
                break     
        else:
            print("ingrese una opcion valida")            
#Funcion para Eliminar un  empleado      
def Eliminar_empleado():
    """
    Funcion que Elimina un usuario a uno de los diccionarios
    
    la funcion pregunta si se desea Eliminar un empeleado. en caso de la respuesta ser "s" se hara una verficacion y depues pedira los 
    datos del empleado como el nombre y el rol. el rol lo pide con 2 opciones, 1 y 2 las cuales son correspondientes a empleado y admnistrador
    luego de ello lo elimina del dicionario.
    
    Variables globales utilizadas:
        Administradores (dict): Diccionario anidado que contiene usuarios administradores y sus claves.
        empleados (dict): Diccionario anidado que contiene usuarios empleados y sus claves.
    
    Manejo de Errores:
        La funcion cuenta con varios manejosde errores para que se ingrese alguno de los datos requeridos. de no ser asi mostrara un error y lo solicitara de nuevo
    
    Flujo:
        1. Pregunta si se desea agregar un empleado:
        2. Valida que la opción sea una de las requeridas.
            -de ser la respuesta "s":
                -solicitara le nombre del empleado
                -solicitara el rol:
                    -Según la opción seleccionada, ejecuta la acción correspondiente.
                    -solicitara la clave        
        3. Si se ingresa un valor no numérico o fuera de rango, muestra un mensaje de error y solicita de nuevo la opción.
    """
    while True:
        confirmar_continuidad= input("Desea Eliminar un empleado?(s/n): ").lower()
        if confirmar_continuidad in ["s","n"]:
            if confirmar_continuidad == "s":
                nombre = input("ingrese el nombre del  empleado a eliminar: ")
                rol_m = input("si es empleado escriba 1 si es admin esrcriba 2: ")
                if rol_m in["1","2"]:
                    if rol_m == "1":
                        del Empleados[nombre] 
                        print("usuario Eliminado")
                        
                    else:
                        del Administradores[nombre] 
                        print("usuario eliminado")
                else:
                    print("ingrese una opcion valida")        
            else:
                print("saliendo...")       
                break     
        else:
            print("ingrese una opcion valida") 
#Funcion que muestra los empleados y los Admins    
def Mostrar_Usuarios():
    #muestra en pantallo tanto los usuarios administradores como los empleados    
    print(f"Los usuarios administradores son :{Administradores}")
    print(f"los usuarios empleados son:{Empleados}")
#Funcion para mostrar las estadisticas de los salarios    
def Mostrar_Estadisticas():
    total=[i[salarios] for i in salarios.values()]
    total_salarios = sum(total)
    media=statistics.mean(total)       
    mediana=statistics.median(total)    
    moda= statistics.mode(total)    
    while True:
            opcion = int(input(
                                "================\n"
                                "1--Total salarios\n"
                                "2--media\n"
                                "3--mediana\n"
                                "4--moda\n"
                                "5--Salir\n"
                                "Opción: "
                                ))   
            match opcion:
                    case 1:
                        print(f"el total de salarios es: {total_salarios}")
                    case 2:
                        print(f"la media es: {media}")
                    case 3:
                        print(f"la mediana es: {mediana}")
                    case 4:
                        print(f"la moda es: {moda}")
                    case 5:
                        print(f"Saliendo")
                        break
                            
                    


    
    pass
def  Mostrar_Estadisticas_empleado():
    pass
login()    