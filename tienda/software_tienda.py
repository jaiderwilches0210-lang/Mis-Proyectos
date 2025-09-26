import random
import sys
from datetime import datetime
productos = {}
stock = {}
ventas = []
monto_minimo = 50000
vendedores = ["Jaider" , "Angie" , "Alejandro", "Juan", "Tomas"]
clave= "ingsoftware123"
descuento = random.randint(5,51)
total = 0
contador_productos = 0

# funciones

def informe_ventas():
    if not ventas:
        print("No hay ventas registradas aún.")
        return
    
    total_ventas = len(ventas)
    suma_total = sum(venta["total"] for venta in ventas)
    
    print(f"Total de ventas realizadas: {total_ventas}")
    print(f"Monto total acumulado de ventas: ${suma_total:.2f}")




def hora_actual():
    ahora = datetime.now()
    return ahora.strftime("%H:%M:%S")

def fecha_actual():
    ahora = datetime.now()
    return ahora.strftime("%d-%m-%Y")     

def login():
    while True:
        terminar_bucle = input("¿Desea  continuar con el login? (s/n): ").lower()

        if terminar_bucle == "n":
            print("Saliendo del login.")
            break

        elif terminar_bucle == "s":
            Nombre_usuario = input("Ingrese el nombre de usuario registrado: ")
            if Nombre_usuario in vendedores:
                clave_ingresada = input("Ingrese la clave: ")
                if clave_ingresada == clave:
                    print("Bienvenido")
                    menu_vendedor()
                else:
                    print("Clave incorrecta")
                    return    
            else:
                print("Usuario no registrado")  
                return

        else:
            print("Opción inválida. Ingrese 's' para salir o 'n' para continuar.")

def agregar_producto():
    while True:
        print("Elegiste la opción: 1 -- Agregar")
        Confirmacion = input("¿Desea agregar un producto? (s/n): ")

        if Confirmacion.lower() == "s":
            nombre_producto = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    precio_producto = float(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Precio inválido. Intente nuevamente.")
            productos[nombre_producto] = precio_producto
            print(f"Nombre asignado: {nombre_producto}, Precio asignado: {precio_producto}")

        elif Confirmacion.lower() == "n":
            print("Lista actual de productos:")
            print(productos)
            break
        else:
            print("Opción no válida. Ingrese 's' o 'n'.")

def Eliminar_producto():
    while True:
        print("Elegiste la opción: 2 -- Eliminar")
        Confirmacion = input("¿Desea eliminar un producto? (s/n): ")

        if Confirmacion.lower() == "s":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            if nombre in productos:
                del productos[nombre]
                print(f"Producto '{nombre}' eliminado.")
            else:
                print(f"El producto '{nombre}' no existe.")
        elif Confirmacion.lower() == "n":
            print("Lista actual de productos:")
            print(productos)
            break
        else:
            print("Opción no válida. Ingrese 's' o 'n'.")

def Editar_producto():
    while True:
        print("Elegiste la opción: 3 -- Editar")
        Confirmacion = input("¿Desea editar un producto? (s/n): ")

        if Confirmacion.lower() == "s":
            nombre_actual = input("Ingrese el nombre actual del producto: ")

            if nombre_actual in productos:
                while True:
                    opcion = input("¿Desea cambiar el nombre (n) o el precio (p)? ").lower()
                    if opcion in ("n", "p"):
                        break
                    else:
                        print("Opción no válida, por favor ingrese 'n' o 'p'.")

                if opcion == "n":
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                    productos[nuevo_nombre] = productos[nombre_actual]
                    del productos[nombre_actual]
                    print(f"Nombre cambiado a '{nuevo_nombre}'.")

                elif opcion == "p":
                    while True:
                        try:
                            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                            break
                        except ValueError:
                            print("Precio inválido. Ingrese un número.")
                    productos[nombre_actual] = nuevo_precio
                    print(f"Precio de '{nombre_actual}' actualizado a {nuevo_precio}.")
            else:
                print("Producto no encontrado.")

        elif Confirmacion.lower() == "n":
            print("Lista actual de productos:")
            print(productos)
            break
        else:
            print("Opción no válida. Ingrese 's' o 'n'.")

def editar_stock():
    if not stock:
        print("Primero debe agregar productos y su stock.")
        return

    while True:
        producto = input("Ingrese el nombre del producto cuyo stock desea modificar: ")
        
        if producto in stock:
            print(f"Stock actual de '{producto}': {stock[producto]}")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
                stock[producto] = nueva_cantidad
                print(f"Stock de '{producto}' actualizado a {nueva_cantidad}.")
                break
            except ValueError:
                print("Cantidad inválida. Debe ingresar un número entero.")
        else:
            print(f"El producto '{producto}' no tiene stock asignado o no existe.")
            opcion = input("¿Desea intentar con otro producto? (s/n): ").lower()
            if opcion != "s":
                break

def agregar_stock():
    if not productos:
        print("Primero debe agregar productos.")
        return
    
    for nombre in productos:
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad en stock para '{nombre}': "))
                stock[nombre] = cantidad
                break
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero.")

def alerta_stock():
    if not stock:
        print("⚠️  Aún no se ha asignado stock a los productos.")
        return
    
    alerta_mostrada = False
    for producto,cantidad in stock.items():
        if cantidad < 10:
                print(f"Alerta el producto : {producto} tiene menos de 10 unidades ")
                alerta_mostrada = True

    if not alerta_mostrada :
            print("✅ Todos los productos tienen suficiente stock.")        

def gestion_de_productos():

    while True:
        alerta_stock()

        try:
            des1 = int(input("Seleccione una opción:\n"
                             "1 -- Agregar\n"
                             "2 -- Eliminar\n"
                             "3 -- Editar\n"
                             "4 -- Agregar stock\n"
                             "5 -- editar stock\n"
                             "6 -- consultar productos\n"
                             "7 -- consultar stock\n"
                             "Ingrese opción: "))
            
            if des1 not in [1, 2, 3, 4, 5, 6, 7]:
                print("Opción no válida. Debe ser 1, 2, 3 , 4, 5, 6, o 7.\n")
                continue  

            if des1 == 1:
                agregar_producto()

            elif des1 == 2:
                Eliminar_producto()

            elif des1 == 3:
                Editar_producto()

            elif des1 == 4:
                agregar_stock()

            elif des1 == 5:
                editar_stock()

            elif des1 == 6:
                if not productos:
                    print("No hay productos registrados.")
                else:
                    print("Lista de productos y precios:")
                    for nombre, precio in productos.items():
                        print(f"Producto: {nombre} - Precio: ${precio:.2f}")

            elif des1 == 7:
                if not stock:
                    print("No hay stock registrado.")
                else:
                    print("Stock disponible por producto:")
                    for nombre, cantidad in stock.items():
                        print(f"Producto: {nombre} - Cantidad: {cantidad}")
            
            break

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (1 a 4).\n")

def promocion():
    global monto_minimo

    while True:
        opcion = input("¿Quieres consultar (c), editar (e) la promoción o salir (s)? ").lower()
        if opcion == "c":
            print(f" Si el total supera ${monto_minimo}, obtendrá un descuento entre 5% y 50%.")
        
        elif opcion == "e":
            try:
                monto_minimo = float(input("Nuevo monto mínimo para descuento: "))
                print("Promoción actualizada.")
            except ValueError:
                print(" Valor inválido. Ingrese solo números.")
        
        elif opcion == "s":
            print("Saliendo del menú de promoción.")
            break
        else:
            print("Opción no válida.")
            
def menu_vendedor():
    while True:
        try:
            des2 = int(input("Seleccione una opción:\n"
                             "1 -- Gestion de productos\n"
                             "2 -- promociones\n"
                              "3 -- informes\n"
                              "4 -- salir\n"   
                              "Ingrese opción: "))
            if des2 not in [1, 2, 3, 4]:
                print("debe ingresar un numero entre 1 y 4")
                continue
            if des2 == 1:
                gestion_de_productos()

            elif des2 == 2:
                promocion()   

            elif des2 == 3:
                informe_ventas()
               
            elif des2 == 4:
                print("saliendo del menu vendedor")
                break    

        except ValueError :
            print("debe ingresar un numero entre 1 y 4")

def eleccion_perfil():
    while True:
        try:
            des3 = int(input("Seleccione una opción:\n"
                                    "1 -- Menu de vendedor\n"
                                    "2 -- Menu de comprador\n"
                                    "3 -- Terminar programa\n"
                                    "ingrese una opcion : "))
            if des3 not in [1,2,3]:
                print("Ingrese un numero entre 1 y 3")
                
            elif des3 == 1 : 
                login()
            elif des3 == 2:
                menu_comprador()    
            elif des3 == 3 :
                print("finalizando programa")
                sys.exit()
        except ValueError:
            print("Ingrese un numero entre 1 y 3")

def compras():
    global total, contador_productos
    contador_productos = 0
    carrito = {}

    while True:
        des6 = input("¿Desea agregar un producto al carrito? (s/n): ").lower()
        if des6 == "s":
            producto_a_comprar = input("Ingrese el nombre exacto del producto: ")
            if producto_a_comprar in productos:
                carrito[producto_a_comprar] = carrito.get(producto_a_comprar, 0) + 1
                total += productos[producto_a_comprar]
                contador_productos += 1
                print(f"Producto agregado. Precio: ${productos[producto_a_comprar]:.2f}. Total parcial: ${total:.2f}")
            else:
                print("Producto no encontrado. Intente de nuevo.")
        elif des6 == "n":
            break
        else:
            print("Seleccione una opción válida (s/n).")

    if contador_productos > 0:
        ventas.append({
            "fecha": fecha_actual(),
            "hora": hora_actual(),
            "productos": carrito.copy(),
            "total": total
        })
        print(f"Compra registrada. Total a pagar: ${total:.2f}")
    else:
        print("No se agregaron productos, no se registró la compra.")

    total = 0
    contador_productos = 0


def recibo():
    print("\n========== RECIBO ==========")
    print("emitido a las : ", hora_actual())
    print("Fecha actual : ", fecha_actual())
    print("subtotal : ", total)
    print("aplica iva del 19% sobre el valor final")
    print("IVA : ", total*0.19)
    print("Total : ",total-total*0.19)

    print("\n=============================")
   
def menu_comprador():
    while True:
        try:
            des5 = int(input("Seleccione una opción:\n"
                             "1 -- Mostrar productos\n"
                             "2 -- comprar\n"
                              "3 -- recibo\n"
                              "4 -- salir\n"   
                              "Ingrese opción: "))
            if des5 not in [1, 2, 3, 4]:
                print("debe ingresar un numero entre 1 y 4")
                continue

            if des5 == 1:
                print(f"los productos son : {productos}")
                print(f"el stock de los productos son : {stock}")

            elif des5 == 2:
                compras()    

            elif des5 == 3:
                recibo()

            elif des5 == 4:
                print("saliendo del menu comprador")
                break    

        except ValueError :
            print("debe ingresar un numero entre 1 y 4")
# estructura principal 

while True:
    eleccion_perfil()

