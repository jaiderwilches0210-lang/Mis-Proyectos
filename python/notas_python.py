# Notas para aprender sobre python
# .........................................................................................................

# Imprimir en pantalla
print("Hola Mundo")
# el print funciona para mostrar en pantalla

Hola = "saludo"
print(f"Variable Hola: {Hola}")
# aqui declaramos una variable y la mostramos en pantalla
# .........................................................................................................s
    #sep
print("Hola", "Mundo", sep=" ")
# el sep es un parametro que se le puede agregar al print para separar los valores que se le pasan al print con el valor que se le indique
    #end
print("Hola", end="23")
# el end es un parametro que se le puede agregar al print para agregar un valor al final del print
    #flush
print("Hola", flush=True)   
# el flush es un parametro que se le puede agregar al print para que se muestre en pantalla inmediatamente despues de ser llamado
    
    #iterador
lista = [10, 20, 30]
iterador = iter(lista)
#nos permite crear un iterador



while True:
    if input("1:"):
        print (next(iterador))
            
        #con el next controlamos el iterador
    else:
        break
    
def saludar():
    yield "Hola"
    yield "¿Cómo estás?"
    yield "Chao"

gen = saludar()

print(next(gen))  # 👉 "Hola"
print(next(gen))  # 👉 "¿Cómo estás?"
print(next(gen))  # 👉 "Chao"
      
# .........................................................................................................
#se puede declarar una variable con un valor muy largo
jiji= "hola, como estas, espero que estes bien, me alegra verte " \
       "por aqui, espero que te guste el contenido que te mostrare"
print(jiji)
# .........................................................................................................
# Tipos de datos
print(f"Tipo de dato de Hola: {type(Hola)}")
# esto nos mostrara el tipo de dato de la variable Hola    

print(f"Tipo de dato de 5: {type(5)}")
# esto nos mostrara el tipo de dato de la variable 5

print(f"Tipo de dato de 5.5: {type(5.5)}")
# esto nos mostrara el tipo de dato de la variable 5.5

print(f"Tipo de dato de True: {type(True)}")
# esto nos mostrara el tipo de dato de la variable True  
    #ord 
print(f"Tipo de dato de 'b': {ord('b')}")
# La función ord() en Python toma un carácter (una cadena de texto de longitud 1) como a
# rgumento y devuelve el valor numérico correspondiente a ese carácter en el sistema de codificación Unicode.

    #hex
print(f"Tipo de dato de 10: {hex(10)}")
# La función hex() en Python toma un número entero como argumento y devuelve su representación en forma de cadena de texto en hexadecimal.
    #oct
print(f"Tipo de dato de 10: {oct(10)}")
# La función oct() en Python toma un número entero como argumento y devuelve su representación en forma de cadena de texto en octal.

a = isinstance("aa", str)
print (a)
#esto nos mostrara si el valor es una instancia de la clase indicada 
ff = "jaider"
ff2 = ff[::-1]
print(ff2)
#esto nos mostrara la palabra al reves


# .........................................................................................................

# Indexacion es la forma de acceder a los elementos de una lista
print(f"Primera letra de Hola: {Hola[0]}")
# esto nos mostrara la letra que que esta en la posicion indicada (0) de la variable Hola             

print(f"Última letra de Hola: {Hola[-1]}")
# esto nos mostrara la ultima letra de la variable Hola

print(f"Letras de Hola de la posición 0 a 4: {Hola[0:4]}")
# esto nos mostrara las letras que estan en las posiciones indicadas (0:4) de la variable Hola

# .........................................................................................................

# Concatenacion es la union de dos o mas cadenas de texto
print(f"Concatenación de Hola y Mundo: {Hola + ' Mundo'}")
# esto nos mostrara la union de la variable Hola y la palabra Mundo 

# .........................................................................................................

# Algunos metodos de las cadenas de texto
print(f"Hola en mayúsculas: {Hola.upper()}")
# esto nos mostrara la variable Hola en mayusculas

print(f"Hola en minúsculas: {Hola.lower()}")
# esto nos mostrara la variable Hola en minusculas                

print(f"Hola con 'saludo' reemplazado por 'despedida': {Hola.replace('saludo', 'despedida')}")
# esto nos mostrara la variable Hola con la palabra saludo reemplazada por la palabra despedida

print(f"Longitud de Hola: {len(Hola)}")
# esto nos mostrara la longitud de la variable Hola

print(f"Hola separada por espacios: {Hola.split(' ')}")
# esto nos mostrara la variable Hola separada por espacios

print(f"Hola sin espacios: {Hola.strip()}")
# esto nos mostrara la variable Hola sin espacios

print(f"Cantidad de veces que se repite 'a' en Hola: {Hola.count('a')}")
# esto nos mostrara la cantidad de veces que se repite la letra 'a' en la variable Hola

print(f"Posición de 'a' en Hola: {Hola.find('a')}")
# esto nos mostrara la posicion de la letra 'a' en la variable Hola

print(f"Hola con la primera letra en mayúscula: {Hola.title()}")
# esto nos mostrara la variable Hola con la primera letra en mayuscula

print(f"Hola con la primera letra en mayúscula: {Hola.capitalize()}")
# esto nos mostrara la variable Hola con la primera letra en mayuscula     

print(f"Hola con mayúsculas y minúsculas intercambiadas: {Hola.swapcase()}")
# esto nos mostrara la variable Hola con las letras en mayusculas en minusculas y viceversa

print(f"Hola centrada en un espacio de 20 caracteres: {Hola.center(20)}")
# esto nos mostrara la variable Hola centrada en un espacio de 20 caracteres

print(f"Hola codificada: {Hola.encode()}")
# esto nos mostrara la variable Hola codificada

print(f"Hola sin espacios a la izquierda: {Hola.lstrip()}")
# esto nos mostrara la variable Hola sin espacios a la izquierda

print(f"Hola sin espacios a la derecha: {Hola.rstrip()}")
# esto nos mostrara la variable Hola sin espacios a la derecha             

print(f"Hola es alfanumérica: {Hola.isalnum()}")
# esto nos mostrara si la variable Hola es alfanumerica

print(f"Hola es alfabética: {Hola.isalpha()}")
# esto nos mostrara si la variable Hola es alfabetica

print(f"Hola es numérica: {Hola.isdigit()}")
# esto nos mostrara si la variable Hola es numerica

print(f"Posición de 'a' en Hola: {Hola.index('a')}")
# esto nos mostrara la posicion de la letra 'a' en la variable Hola       

# .........................................................................................................

# Jerarquia de operaciones
# PEMDAS
# Parentesis
# Exponentes
# Multiplicacion y division
# Adicion y sustraccion
# ese es el orden en el que se operan las ecuaciones

a = 5
b = 10

operacion = 5 + 10 * 2
print(f"Resultado de 5 + 10 * 2: {operacion}")    
# primero se multiplica 10 por 2 y despues se suma 5

operacion2 = (5 + 10) * 2
print(f"Resultado de (5 + 10) * 2: {operacion2}")
# primero se suman 5 y 10 y despues se multiplica por 2

# .........................................................................................................

# Operaciones aritmeticas
print(f"Suma de a y b: {a + b}")
# esto nos mostrara la suma de las variables a y b  

print(f"Resta de a y b: {a - b}")
# esto nos mostrara la resta de las variables a y b

print(f"Multiplicación de a y b: {a * b}")
# esto nos mostrara la multiplicacion de las variables a y b

print(f"Potencia de a y b: {a ** b}")
# esto nos mostrara la potencia de las variables a y b

print(f"División de a y b: {a / b}")
# esto nos mostrara la division de las variables a y b

print(f"División entera de a y b: {a // b}")
# esto nos mostrara la division entera de las variables a y b

print(f"Residuo de la división de a y b: {a % b}")
# esto nos mostrara el residuo de la division de las variables a y b

print(f"a es igual a b: {a == b}")
# esto nos mostrara si las variables a y b son iguales    

print(f"a es diferente de b: {a != b}")
# esto nos mostrara si las variables a y b son diferentes

print(f"a es mayor que b: {a > b}")
# esto nos mostrara si la variable a es mayor que la variable b

print(f"a es menor que b: {a < b}")
# esto nos mostrara si la variable a es menor que la variable b

print(f"a es mayor o igual que b: {a >= b}")
# esto nos mostrara si la variable a es mayor o igual que la variable b

print(f"a es menor o igual que b: {a <= b}")
# esto nos mostrara si la variable a es menor o igual que la variable b

a += b
print(f"Nuevo valor de a después de a += b: {a}")
# el signo al estar antes de la igualdad significa que se operara la variable b a la variable a   

# .........................................................................................................

# Input
nombre = input("Cual es tu nombre?")
print(f"Nombre ingresado: {nombre}")
# esto nos mostrara un mensaje en pantalla y nos pedira que ingresemos un valor

# .........................................................................................................

# Convertir tipos de datos
numero = int(input("ingresa un numero"))
print(f"Número entero ingresado: {numero}")
# esto nos mostrara un mensaje en pantalla y nos pedira que ingresemos un valor y lo convertira en un numero entero

numero2 = float(input("ingresa un numero"))
print(f"Número flotante ingresado: {numero2}")
# esto nos mostrara un mensaje en pantalla y nos pedira que ingresemos un valor y lo convertira en un numero flotante

# .........................................................................................................

# Listas
lista = ["hola", 5, 5.5, True]
# esto es una lista que contiene diferentes tipos de datos

print(f"Lista completa: {lista}")
# accesar a la lista

print(f"Primer elemento de la lista: {lista[0]}")
# esto nos mostrara el primer elemento de la lista

print(f"Último elemento de la lista: {lista[-1]}")
# esto nos mostrara el ultimo elemento de la lista

print(f"Elementos de la lista en las posiciones 0 a 2: {lista[0:2]}")
# esto nos mostrara los elementos de la lista en las posiciones indicadas

# Modificar elementos de la lista
lista[0] = "adios"
print(f"Lista después de modificar el primer elemento: {lista}")
# esto cambiara el valor del primer elemento de la lista

lista.append("hola")
print(f"Lista después de agregar un elemento al final: {lista}")
# esto agregara un elemento al final de la lista

lista.insert(1, "mundo")
print(f"Lista después de insertar un elemento en la posición 1: {lista}")
# esto agregara un elemento en la posicion indicada

lista.pop()
print(f"Lista después de eliminar el último elemento: {lista}")
# esto eliminara el ultimo elemento de la lista

lista.remove("adios")
print(f"Lista después de eliminar el elemento 'adios': {lista}")
# esto eliminara el elemento indicado de la lista

lista.clear()
print(f"Lista después de eliminar todos los elementos: {lista}")
# esto eliminara todos los elementos de la lista

lista = ["hola", "mundo"]
del lista[1]
print(f"Lista después de eliminar el elemento en la posición 1: {lista}")
# esto eliminara el elemento en la posicion indicada de la lista

lista = ["hola", "mundo"]
print(f"Posición del elemento 'hola' en la lista: {lista.index('hola')}")
# esto nos mostrara la posicion del elemento indicado

numeros = [1, 2, 3, 4, 5, 312312, 7, 8, 9, 10]  
print(f"Número mayor de la lista: {max(numeros)}")
# esto nos mostrara el numero mayor de la lista  

print(f"Número menor de la lista: {min(numeros)}")
# esto nos mostrara el numero menor de la lista

print(f"Cantidad de veces que se repite el número 5 en la lista: {numeros.count(5)}")
# esto nos mostrara cuantas veces se repite el numero indicado

numeros.sort()
print(f"Lista ordenada de menor a mayor: {numeros}")
# esto ordenara la lista de menor a mayor

numeros.sort(reverse=True)
print(f"Lista ordenada de mayor a menor: {numeros}")
# esto ordenara la lista de mayor a menor

# .........................................................................................................

# Metodo slicing
#el metodo slicing es una forma de acceder a los elementos de una lista de una forma mas sencilla
aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bb = aa[:]
print(f"Lista bb copiada de aa: {bb}")
# esto copiara la lista aa en la lista bb

aa.append(11)
print(f"Lista aa después de agregar un elemento: {aa}")
print(f"Lista bb después de modificar aa: {bb}")
# aqui lo que hacemos es fijar copiar el valor de aa y fijarlo para que al modificar aa no se modifique bb

# .........................................................................................................

# Listas de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Primer elemento de la primera lista en la matriz: {matriz[0][0]}")
# esto nos mostrara el primer elemento de la primera lista

# .........................................................................................................

# Tuplas
numeros = (1, 2, 3, 4, 5)
print(f"Tupla completa: {numeros}")
# esto es una tupla
# las tuplas son inmutables, no se pueden modificar

# .........................................................................................................

# Diccionarios
numeros1 = {"uno": 1, "dos": 2, "tres": 3}
print(f"Diccionario completo: {numeros1}")
# esto es un diccionario
# los diccionarios son clave-valor

del numeros1["uno"]
print(f"Diccionario después de eliminar el elemento 'uno': {numeros1}")
# esto eliminara el elemento indicado del diccionario
# los diccionarios no tienen orden
# los diccionarios no pueden tener claves repetidas

print(f"Claves del diccionario: {numeros1.keys()}")
# esto nos mostrara las claves del diccionario

print(f"Valores del diccionario: {numeros1.values()}")
# esto nos mostrara los valores del diccionario         

print(f"Elementos del diccionario: {numeros1.items()}")
# esto nos mostrara los elementos del diccionario de dos en 2 (clave y valor)

# .........................................................................................................

# Diccionario de diccionarios
contactos = {
    "contacto1": {"nombre": "juan", "telefono": 1234567890},
    "contacto2": {"nombre": "pedro", "telefono": 987654321}
}
print(f"Nombre del contacto1: {contactos['contacto1']['nombre']}")
# esto es un diccionario de diccionarios

# ...........................................................................................................................................
    #args
def mi_funcion(*args):
    for arg in args:
        print(arg)

mi_funcion(1, 2, 3, 4)
# los args son una forma para que la funcion reciba un número variable de argumentos posicionales (es decir, valores que se pasan sin nombre). 
# Los valores que pasas a la función con *args se recogen como una tupla dentro de la función.
# ...........................................................................................................................................
    #kwargs
#ejemplo sencillo
def mi_funcion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mi_funcion(nombre="Jaider", edad=20)        

    
# los kwargs son una forma para que la función reciba un número variable de argumentos de palabra clave (es decir, argumentos que se pasan con un nombre).
# Los valores que pasas a la función con **kwargs se recogen como un diccionario dentro de la función.
# .........................................................................................................

# Estructuras condicionales
x = 10

# if
if x < 5:
    print("x es menor que 5")
# en el caso de que x sea menor que 5 se ejecutara el print

# else
if x < 5:
    print("x es menor que 5")
else:
    print("x es mayor o igual que 5")
# en el caso de que x sea menor que 5 se ejecutara el primer print y en caso contrario se ejecutara el segundo

# elif
if x < 5:
    print("x es menor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es igual a 10")
# en el caso de que x sea menor que 5 se ejecutara el primer print, si x es igual a 5 se ejecutara el segundo y si no se ejecutara el tercero

# .........................................................................................................

if x > 1 and x < 10:
    print("x es mayor que 1 y menor que 10")
# en el caso de que x sea mayor que 1 y menor que 10 se ejecutara el print

if x > 1 or x < 10:
    print("x es mayor que 1 o menor que 10")
# en el caso de que x sea mayor que 1 o menor que 10 se ejecutara el print

if not(x == 10):
    print("x no es igual a 10")
# en el caso de que x no sea igual a 10 se ejecutara el print

# .........................................................................................................
    #match
r = 189
match r:
    case 189 | 190:
        print("valor correcto")
        
    case _ if r < 189:
        print("incorrecto")
    case _ if r > 190:
        print("incorrecto") 
        #es una estructura para no tener que usar estructuras if tan largas

        #ejemplo con for
for i in range(10):
    match i:
        case 0:
            print("cero")
        case _ if not 0:
            print("no es cero")
        #esto es un ejemplo de como se puede usar el match con un for    

# .........................................................................................................

# Bucles y control de iteraciones
# for
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(f"El valor de i es: {i}")    
# esto nos mostrara el valor de i en cada iteracion del bucle

for i in range(5, 10):
    print(f"El nuevo valor de i es: {i}")
# esto nos mostrara el valor de i en cada iteracion del bucle, usando el metodo range le indicamos o controlamos la iteracion

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        print("banana encontrada")
# esto nos mostrara si la fruta banana esta en la lista usando un condicional dentro del bucle for
# range(stop)

# rango(3)

# rango(3+1)

# rango(inicio, parada)

# rango(2, 6)

# rango(5,10+1)

# rango(inicio, parada, paso)

# rango(4, 15+1, 2)

# rango(2*2, 25, 3+2)

# rango(10, 0, -2)
# while
i = 1
while i < 6:
    print(i)
    i += 1
# esto se realizara mientras i sea menor que 6 y se ira sumando 1 en cada iteracion hata que i sea igual a 6
    
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
# esto se realizara mientras i sea menor que 6 y se ira sumando 1 en cada iteracion hata que i sea igual a 6, pero si i es igual a 3 se detendra el bucle

numeros = [1, 2, 3, 4, 5]
for i in numeros:
    if i == 3:
        continue
    print(i)
# esto nos mostrara los numeros de la lista, pero si el numero es igual a 3 se saltara ese numero y continuara con el siguiente
     #break
for i in numeros:
    if i == 3:
        break
    print(i)
    #esto nos mostrara los numeros de la lista, pero si el numero es igual a 3 se detendra el bucle

    #continue
for i in numeros:
    if i == 3:
        continue
    print(i)
    #esto nos mostrara los numeros de la lista, pero si el numero es igual a 3 se saltara ese numero y continuara con el siguiente
    
    #pass

for i in numeros:
    if i == 3:
        pass
    print(i)
    #esto nos mostrara los numeros de la lista, pero si el numero es igual a 3 no hara nada y continuara con el siguiente     

import time
start = time.time()
print(round(time.time() - start, 2))

    #enumerate
enumerate_list = ["a", "b", "c", "d"]
for i, value in enumerate(enumerate_list):
    print(f"Index: {i}, Value: {value}")
    #esto nos mostrara el index y el valor de cada elemento de la lista dandole enumeracion asi como dice su nombre
# .........................................................................................................

# Generadores e iteradores
my_list = [1, 2, 3, 4, 5]   

my_iter = iter(my_list)
print(f"Primer elemento de la lista: {next(my_iter)}")
# esto nos mostrara el primer elemento de la lista

print(f"Segundo elemento de la lista: {next(my_iter)}")
# esto nos mostrara el segundo elemento de la lista y asi sucecivamente

# tambien lo podemos hacer con texto
my_str = "Hola"
my_iter = iter(my_str)
print(f"Primera letra de la palabra: {next(my_iter)}")
# esto nos mostrara la primera letra de la palabra

print(f"Segunda letra de la palabra: {next(my_iter)}")
# esto nos mostrara la segunda letra de la palabra y asi sucecivamente
limite=10
iterador=iter(range(1,limite+1,2))
# asi funciona la syntaxis:
    # range(start, stop, step)
    # start: por donde empieza
    # stop: donde para limit+1 = 10
    # step: numero de posiciones que avanza

for i in iterador:
    print(i)
# esto nos mostrara los numeros impares del 1 al 10( esto funciona asi: 
# primero se le indica el rango de numeros que se mostraran, despues se le indica que se mostraran los 
# numeros de 2 en 2 y despues se le indica que se mostraran los numeros impares)
#ahora lo haremos con los pares
iterador2=iter(range(0,limite+1,2))
for i in iterador2:
    print(i)
    # recorre cada elemento del iterador y toma cada nuevo valor que arroja el iterador
# esto nos mostrara los numeros pares del 1 al 10( esto funciona asi:
# primero se le indica el rango de numeros que se mostraran, despues se le indica que se mostraran los
# numeros de 2 en 2 y despues se le indica que se mostraran los numeros pares)

# .........................................................................................................

    #generadores
def generador():    
    yield 1
    yield 2
    yield 3 
    #el yield es una palabra clave que se utiliza como return, excepto que la funcion devolvera un generador
# esto es un generador que nos retornara o le dara valor a la funcion de los numeros 1, 2 y 3

for G in generador():
    print(G)
# esto nos mostrara los valores del generador en cada iteracion

# .........................................................................................................

    #funciones
def saludar(jadier):
    print(f"Hola {jadier}")
saludar("jaider")
    #aqui se define una funcion que recibe un parametro y lo imprime

#se pueden poner mas de una variable dentro de la funcion

def jugador(nombre, numero):
    print(f"El jugador {nombre} tiene el numero {numero}")
jugador("jaider", 10)
    #aqui se define una funcion que recibe dos parametros y los imprime

#ejercicio calculadora
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def calculadora():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = int(input("Ingrese una opción: (1|2|3|4|5)"))
        if option == 5:
            break
        if option not in (1,2,3,4,5):
            print("Opción no valida")
            
        elif option in (1,2,3,4,5):
            num1= float(input("Ingrese el primer número: "))
            num2= float(input("Ingrese el segundo número: ")) 

            if option == 1:
                print(f"La suma de {num1} y {num2} es: {suma(num1, num2)}")
            elif option == 2:
                print(f"La resta de {num1} y {num2} es: {resta(num1, num2)}")
            elif option == 3:
                print(f"La multiplicación de {num1} y {num2} es: {multiplicacion(num1, num2)}")
            elif option == 4:
                print(f"La división de {num1} y {num2} es: {division(num1, num2)}")

        else:
            print("Opción no valida")

calculadora()
#esto es una calculadora que suma, resta, multiplica y divide dos numeros
#. .........................................................................................................
    
    #funciones anonimas

add = lambda a, b: a + b
print(add(5, 3))
# la funcion lambda es una manera rapida de crear funciones anonimas(sin tener que nombrar de manera tradicional la funcion)
# en este caso la funcion lambda recibe dos parametros y los suma

mensaje = lambda mensaje: mensaje("Hola Mundo")
print(mensaje(lambda mensaje: mensaje))
# en este caso la funcion lambda recibe un parametro y lo imprime

# ..............................................................................................................................................
    #set
conjunto = {1, 2,2, 3, 4, 5}
print(conjunto)
# los conjuntos son colecciones desordenadas de elementos unicos
    #metodos de conjuntos
conjunto.add(6)
print(conjunto)
# el metodo add agrega un elemento al conjunto
conjunto.remove(6)
print(conjunto)
# el metodo remove elimina un elemento del conjunto
conjunto.clear()
print(conjunto)
# el metodo clear elimina todos los elementos del conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto.union(conjunto2))
# el metodo union une dos conjuntos .tambien se puede usando el simbolo de pipe (|)
print(conjunto.intersection(conjunto2))
# el metodo intersection nos mostrara los elementos que se repiten en los dos conjuntos
print(conjunto.difference(conjunto2))
# el metodo difference nos mostrara los elementos que no se repiten en los dos conjuntos
print(conjunto.symmetric_difference(conjunto2))
# el metodo symmetric_difference nos mostrara los elementos que no se repiten en los dos conjuntos

# ..................................................................................................................................................
    #scooping de funciones
def get_total(a, b):
    #enclosed variable: declarada dentro de una funcion pero utilizada en una funcion interna 
    total = a + b

    def double_it():
        #local variable: declarada dentro de una funcion y utilizada solo en esa funcion
        double = total * 2
        print(double)

    double_it()
    #double variable no se podra utilizar fuera de la funcion double_it
   #print(double)

    return total

#..................................................................................................................................................
    

    #MAP
numerous = [1, 2, 3, 4, 5]
cuadrado = list(map(lambda x: x ** 2, numerous))
print(" cuadrados : ", cuadrado)
# map que aplica una funcion a cada elemento de un iterable y devuelve un objeto map 

    #FILTER
pares = list(filter(lambda x: x % 2 == 0, numerous))
print("pares : ", pares)    
# filter que filtra los elementos de un iterable que cumplan con una condicion
#en este caso la condicion de filter es el lamda que dice que si el numero es par lo filtre

    #REDUCE
from functools import reduce   
suma = reduce(lambda x, y: x + y, numerous)
print("suma : ", suma)
# reduce que aplica una funcion a todos los elementos de un iterable
#en este caso la funcion es una suma de todos los elementos de la lista
# ..............................................................................................................................................
    #exepciones
try:
    print(5/0)  
except Exception as e:
    print(e)  
    #esto nos mostrara un mensaje de error si se produce una excepcion 
    print(e.__class__)
    #esto nos dira que tipo de error se produjo
    print(e.__class__.__name__)
    #esto nos mostrara el nombre del error

    #zero division error
try:
    print(5/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
    #esto es un ejemplo de una excepcion que se produce cuando se intenta dividir por cero
    #en este caso se imprime un mensaje diciendo que no se puede dividir por cero
    
    #value error
try:
    int("a")
except ValueError:
    print("No se puede convertir una letra a un numero")
    #esto es un ejemplo de una excepcion que se produce cuando se intenta convertir una letra a un numero
    #en este caso se imprime un mensaje diciendo que no se puede convertir una letra a un numero
#. ..............................................................................................................................................
    #coneccion entre archivos
file = open("hola.txt", mode ="r")

data = file.readlines()
print(data)
file.close()
#esto nos mostrara el contenido de un archivo de texto

with open("hola.txt", mode="r") as file:
    data = file.readlines()
    print(data)
#esto nos mostrara el contenido de un archivo de texto con el with
#ya que el with se encarga de cerrar el archivo despues de que se termine de usar
# ..............................................................................................................................................
    # ..............................................................................................................................................
        #escritura en archivos
    #r= lectura
    #w= escritura
    #a= añadir

    with open("hola.txt", mode="w") as file:
        file.write("Hola Mundo\nEsta es la segunda linea\nY esta la tercera")
    #esto escribira en un archivo de texto  
    with open("hola.txt", mode="a") as file:
        file.write("\nHola Mundo")
    #esto escribira en un archivo de texto pero no borrara el contenido anterior
    try:
        with open("hola.txt", mode="a") as file:
            file.write("\nHola Mundo")
    except FileNotFoundError as e:
        print("El archivo no existe", e)
    #esto es un ejemplo de una excepcion que se produce cuando se intenta abrir un archivo que no existe
    #en este caso se imprime un mensaje diciendo que el archivo no existe
    # ..............................................................................................................................................
        #lectura de archivos 
    with open("hola.txt", mode="r") as file:
        data = file.readlines()
        for line in data:
            print(line.strip())
    #esto nos mostrara el contenido de un archivo de texto linea por linea
    # ..............................................................................................................................................
               
       #QUE ES LA PROGRMACION FUNCIONAL
    #La programación funcional es un paradigma de programación que trata de resolver problemas de la misma forma que las matemáticas.
    #En la programación funcional, las funciones son ciudadanos de primera clase, lo que significa que pueden ser asignadas a variables,
    #pasadas como argumentos y devueltas como valores de otras funciones.

        #FUNCIONES PURAS
    #Una función pura es una función que, dada la misma entrada, siempre devolverá la misma salida y no tiene efectos secundarios.
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    resultado = factorial(5)  # Siempre devolverá 120
    print(resultado)
    # esta es una funcion pura ya que siempre devolvera el mismo resultado si se le pasa el mismo valor
        #FUNCION IMPURA
    #Una función impura es una función que puede devolver diferentes valores para la misma entrada o tiene efectos secundarios.

    contador = 0  # Variable global

    def incrementar_contador():
        global contador
        contador += 1  # Modifica una variable externa
        return contador

    print(incrementar_contador())  # Resultado cambia en cada ejecución
    print(incrementar_contador())  # Ahora devuelve un número mayor

    # ..............................................................................................................................................
        #Recursion 
    #la recursividad es un concepto en el que una función se llama a sí misma para resolver un problema.  


    #. ..............................................................................................................................................
         #comprension de listas
         #sintaxis:
            #[expresion for elemento in iterable | if condicion]
            # list = [ function() for <item> in <list> ]
    a = [1, 2, 3, 4, 5]
    b = [i * 2 for i in a]  # Multiplica cada elemento por 2
    print(b)
         #comprension de diccionarios
            #sintaxis:
                #{clave: valor for variable in iterable | if condicion}
                #dict = { key : value for <item> in <list> }
    a = {"a": 1, "b": 2, "c": 3}    
    b = {k: v * 2 for k, v in a.items()}  # Multiplica cada valor por 2
    print(b)

    #..............................................................................................................................................
        #PROGRAMACION ORIENTADA A OBJETOS
    #La programación orientada a objetos (POO) es un paradigma de programación que se basa en objetos y clases.
    #se usa para estructurar un programa de manera más clara y eficiente.
       
        #CLASES
        # Una clase es un plano para crear objetos.
    class Persona:
        a=5
        print("Hola Mundo")
    nyc = Persona()
    print(nyc.a)
    #esto nos mostrara el valor de la variable a de la clase Persona que es 5 y el mensaje Hola Mundo
       
        #OBJETOS
        # Un objeto es una instancia de una clase.  
    class heroes:
        def __init__(self, nombre, id):
            self.nombre = nombre
            self.id = id
            nombre = "Jaider"# esto es un objeto de la clase heroes
            id = 123# esto es un objeto de la clase heroes
        def mostrar(self):
            print(f"Nombre: {self.nombre}, ID: {self.id}")
            #esto solo imprime el nombre y el id del objeto
        #init
        # El método __init__ es un método especial que se llama cuando se crea un objeto.
        # Se utiliza para inicializar los atributos de un objeto.
        
    class Recipe:
        def __init__(self, nombre, ingredientes) :
            self.nombre = nombre
            self.ingredientes = ingredientes
        def contents(self):
            print(f"Nombre: {self.nombre}")
            print(f"Ingredientes:{self.ingredientes}")
    pizza = Recipe("Pizza", ["Harina", "Tomate", "Queso"])   
    #estos son los objeto de la clase Recipe
    print(pizza.ingredientes)
    print(Recipe.contents(pizza))

        #__NEW__
        # El método __new__ es un método especial que se llama antes de __init__.
        # Se utiliza para crear un nuevo objeto.
        # El método __new__ es un método de clase, lo que significa que se llama en la clase en lugar de en una instancia de la clase.


    class ContadorObjetos:
        contador = 0  # Variable de clase para contar objetos

    def __new__(cls):
        cls._contador += 1  # Aumentamos el contador antes de crear el objeto
        instancia = super().__new__(cls)  # Creamos el objeto normalmente
        return instancia  # Devolvemos la nueva instancia

    def __init__(self):
        print(f"Objeto número {self._contador} creado")
        print(f"Objeto número {ContadorObjetos.contador} creado")
        #esto es un ejemplo de como se usa el metodo __new__

# Crear objetos de la clase
obj1 = ContadorObjetos()  # Salida: Objeto número 1 creado
obj2 = ContadorObjetos()  # Salida: Objeto número 2 creado
obj3 = ContadorObjetos()  # Salida: Objeto número 3 creado


    # ..............................................................................................................................................

        #HERENCIA
        #herencia simple
            #la herencia simple es un concepto en el que una clase hereda atributos y métodos de otra clase.
        #Herencia multiple
            #la herencia multiple es un concepto en el que una clase hereda atributos y metodos de mas de una clase.
        #herencia jerarquica
            #la herencia jerarquica es un concepto en el que una clase hereda atributos y metodos de una clase padre y esta a su vez hereda de otra clase padre.
        #herencia hibrida
            #la herencia hibrida es un concepto en el que una clase hereda atributos y metodos de una clase padre y esta a su vez hereda de mas de una clase padre.
        #herencia multinivel
            #la herencia multinivel es un concepto en el que una clase hereda atributos y metodos de una clase padre y esta a su vez hereda de una clase hija.
    # La herencia es un concepto en el que una clase hereda atributos y métodos de otra clase.
class empleados:
        def __init__(self, nombre, salario):
            self.nombre = nombre
            self.salario = salario
class supervisor(empleados):
        def __init__(self, nombre, salario, contraseña):
            super().__init__(nombre, salario)#el metodo super() se usa para llamar al metodo __init__ de la clase padre
        
            self.contraseña = contraseña
class programador(empleados):
        def leave_request(self, dias):
            return f"{self.nombre} ha solicitado {dias} días de vacaciones"
        #esto es un ejemplo de herencia
adrian = supervisor("Adrian", 50000, "1234")
juan = programador("Juan", 30000)
print(adrian.nombre)
print(juan.leave_request(5))#el 5 el cual hace referencia a los dias de vacaciones solicitados
#este es un ejemplo de herencia en el que la clase supervisor hereda atributos y metodos de la clase empleados
#. ..............................................................................................................................................
    
    #POLIMORFISMO
    #El polimorfismo es un concepto en el que una clase puede tener diferentes formas.

class Perro:
    def sonido(self):
        return "Guau Guau"

class Gato:
    def sonido(self):
        return "Miau Miau"

# Función que usa polimorfismo
def hacer_sonido(animal):
    return animal.sonido()

# Crear instancias
perro = Perro()
gato = Gato()

# Usamos la misma función para ambos objetos
print(hacer_sonido(perro))  # Guau Guau
print(hacer_sonido(gato))   # Miau Miau




# .........................................................................................................................................
    #clases y metodos abstractos
from abc import ABC, abstractmethod
class Animal(ABC):#aqui definimos la clase abstracta
    @abstractmethod
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")#aui generamos el metodo hacer_sonido para la clase perro hereando de la clase animal
miperro = Perro()
print(miperro.hacer_sonido())        

# ..............................................................................................................................................                
#metodos para saber las herencias de una clase

# 1. issubclass(Sub, Super)
# Verifica si una clase es subclase de otra.

class Animal:
    pass

class Perro(Animal):
    pass

print(issubclass(Perro, Animal))  # True, porque Perro hereda de Animal
print(issubclass(Animal, Perro))  # False, Animal no hereda de Perro
print(issubclass(Perro, object))  # True, todas las clases heredan de object

# 2. isinstance(obj, Clase)
# Verifica si un objeto es instancia de una clase o sus superclases.

mi_perro = Perro()
print(isinstance(mi_perro, Perro))  # True, mi_perro es instancia de Perro
print(isinstance(mi_perro, Animal))  # True, porque Perro hereda de Animal
print(isinstance(mi_perro, object))  # True, todas las clases en Python heredan de object
print(isinstance(mi_perro, int))  # False, no es un entero

# 3. dir(obj)
# Muestra los atributos y métodos de un objeto.

print(dir(mi_perro))  # Muestra los atributos y métodos disponibles en mi_perro

# 4. Clase.__bases__
# Muestra las clases base de una clase.

print(Perro.__bases__)  # (<class '__main__.Animal'>,)

# 5. Clase.__mro__ o Clase.mro()
# Muestra el orden de resolución de métodos (Method Resolution Order - MRO).
#help
# Muestra la documentación de una clase o función.
class Animal:
    """Clase base para los animales."""
    pass

class Perro(Animal):
    """Clase que representa un perro."""
    pass

help(Perro)
#aqui el help nos mostrara la documentacion de la clase perro
# ..............................................................................................................................................

    #MODULOS
# Un módulo es un archivo de Python que contiene definiciones y declaraciones.
# Los módulos se utilizan para organizar el código y hacerlo más fácil de mantener.
# Los módulos se pueden importar en otros módulos o scripts de Python para reutilizar el código.
#. ..............................................................................................................................................
    #SYS
    # El módulo sys proporciona funciones y variables que interactúan con el intérprete de Python.
import sys

# 1. sys.argv - Lista de argumentos pasados al script
print("Argumentos del script:", sys.argv)

# 2. sys.exit - Termina el programa con un código de salida (comentado para evitar cierre)
# sys.exit(0)

# 3. sys.path - Lista de rutas donde Python busca módulos
print("\nRutas de búsqueda de módulos:", sys.path)

# 4. sys.version - Muestra la versión de Python en ejecución
print("\nVersión de Python:", sys.version)

# 5. sys.platform - Indica el sistema operativo
print("\nSistema operativo:", sys.platform)

# 6. sys.stdin, sys.stdout, sys.stderr - Entrada, salida y error estándar
print("\nUsando sys.stdout para imprimir este mensaje.")
sys.stderr.write("Esto es un mensaje de error en sys.stderr\n")

# 7. sys.getsizeof - Devuelve el tamaño en bytes de un objeto
mi_lista = [1, 2, 3, 4, 5]
print("\nTamaño en bytes de mi_lista:", sys.getsizeof(mi_lista))

# 8. sys.modules - Diccionario con los módulos importados en el programa
print("\nMódulos actualmente importados:", list(sys.modules.keys())[:10], "...")  # Muestra solo los primeros 10

# 9. sys.executable - Ruta del ejecutable de Python
print("\nRuta del ejecutable de Python:", sys.executable)

# 10. sys.getrecursionlimit - Obtiene el límite de recursión
print("\nLímite de recursión actual:", sys.getrecursionlimit())

# 11. sys.setrecursionlimit(n) - Cambia el límite de recursión (Úsalo con cuidado)
# sys.setrecursionlimit(2000)  # Aumenta el límite a 2000 (descomentarlo si lo necesitas)

# 12. sys.maxsize - Representa el mayor número entero soportado por Python en el sistema
print("\nMáximo tamaño de un entero:", sys.maxsize)

# 13. sys.byteorder - Indica el orden de los bytes en la arquitectura del sistema ('little' o 'big')
print("\nOrden de los bytes en este sistema:", sys.byteorder)

# 14. sys.getdefaultencoding - Obtiene la codificación de caracteres por defecto
print("\nCodificación por defecto:", sys.getdefaultencoding())

# 15. sys.getfilesystemencoding - Devuelve la codificación usada para los nombres de archivos
print("\nCodificación del sistema de archivos:", sys.getfilesystemencoding())

# 16. sys.implementation - Información sobre la implementación de Python en uso
print("\nInformación sobre la implementación de Python:", sys.implementation)

# 17. sys.thread_info - Información sobre la implementación de subprocesos
print("\nInformación sobre subprocesos:", sys.thread_info)

# 18. sys.float_info - Información sobre la precisión y rango de los números flotantes
print("\nInformación sobre números flotantes:", sys.float_info)

# 19. sys.int_info - Información sobre la implementación de enteros en Python
print("\nInformación sobre enteros:", sys.int_info)

# 20. sys.hash_info - Información sobre el algoritmo de hashing usado en Python
print("\nInformación sobre hashing:", sys.hash_info)
#. ..............................................................................................................................................
import calendar


# 1. Mostrar el calendario de un mes específico
print("Calendario de marzo 2025:")
print(calendar.month(2025, 3))

# 2. Mostrar el calendario de un año completo
print("\nCalendario completo de 2025:")
print(calendar.calendar(2025))

# 3. Verificar si un año es bisiesto
print("\n¿2024 es bisiesto?", calendar.isleap(2024))

# 4. Contar los años bisiestos entre dos años
print("\nAños bisiestos entre 2000 y 2030:", calendar.leapdays(2000, 2030))

# 5. Obtener el día de la semana de una fecha específica
print("\nEl 14 de marzo de 2025 es:", calendar.weekday(2025, 3, 14))  # 4 (viernes)

# 6. Mostrar los nombres cortos de los días de la semana (3 letras)
print("\nDías de la semana en formato corto:", calendar.weekheader(3))

# 7. Obtener el primer día de la semana actual (0 = lunes)
print("\nPrimer día de la semana por defecto:", calendar.firstweekday())

# 8. Cambiar el primer día de la semana a domingo
calendar.setfirstweekday(6)  # 6 = domingo
print("Nuevo primer día de la semana:", calendar.firstweekday())

# 9. Obtener información sobre un mes (día de inicio y cantidad de días)
inicio, dias = calendar.monthrange(2025, 3)
print(f"\nMarzo 2025 empieza en el día {inicio} (0 = lunes) y tiene {dias} días.")

# 10. Obtener una matriz representando el mes
print("\nMatriz del mes de marzo 2025:")
for semana in calendar.monthcalendar(2025, 3):
    print(semana)  # Lista de semanas, los días vacíos son 0

#. ..............................................................................................................................................
#MÓDULO OS - Operaciones del sistema operativo

import os

print("\n🔹 MÓDULO OS")
print("Directorio actual:", os.getcwd())  # Obtener el directorio actual
print("Archivos en el directorio:", os.listdir())  # Listar archivos y carpetas
print("Nombre del sistema operativo:", os.name)  # Nombre del sistema operativo
print("Variable de entorno PATH:", os.environ.get("PATH"))  # Obtener variable de entorno

# ..............................................................................................................................................

# MÓDULO TIME - Manejo de tiempos y retrasos

import time

print("\n🔹 MÓDULO TIME")
print("Hora actual en segundos desde 1970:", time.time())
print("Fecha y hora actual:", time.ctime())
time.sleep(1)  # Pausa el programa 1 segundo
print("Después de 1 segundo...")

# ..............................................................................................................................................

# MÓDULO DATETIME - Manejo de fechas y horas
import datetime

print("\n🔹 MÓDULO DATETIME")

now = datetime.datetime.now()
print("Fecha y hora actual:", now)#esto nos mostrara la fecha y hora actual

print("Año:", now.year, "Mes:", now.month, "Día:", now.day)#esto nos mostrara el año, mes y dia actual

future = now + datetime.timedelta(days=10)#esto nos mostrara la fecha dentro de x dias
print("Fecha dentro de 10 días:", future)

# ..............................................................................................................................................

#  MÓDULO RANDOM - Generación de números aleatorios

import random

print("\n🔹 MÓDULO RANDOM")

print("Número aleatorio entre 1 y 100:", random.randint(1, 100))#esto nos mostrara un numero aleatorio entre 1 y 100

print("Número aleatorio decimal entre 0 y 1:", random.random())#esto nos mostrara un numero aleatorio decimal entre 0 y 1
lista = [1, 2, 3, 4, 5]
print("Elemento aleatorio de una lista:", random.choice(lista))#esto nos mostrara un elemento aleatorio de la lista

# ..............................................................................................................................................

# MÓDULO MATH - Operaciones matemáticas avanzadas
import math

print("\n🔹 MÓDULO MATH")
print("Raíz cuadrada de 16:", math.sqrt(16))#esto nos mostrara la raiz cuadrada de 16
print("Valor de pi:", math.pi)#esto nos mostrara el valor de pi
print("Seno de 45°:", math.sin(math.radians(45)))#esto nos mostrara el seno de 45 grados
print("Logaritmo natural de 10:", math.log(10))#esto nos mostrara el logaritmo natural de 10

# ..............................................................................................................................................

# 7️⃣ MÓDULO STATISTICS - Estadísticas y cálculos matemáticos
import statistics

print("\n🔹 MÓDULO STATISTICS")
datos = [10, 20, 30, 40, 50]
print("Media:", statistics.mean(datos))#esto nos mostrara la media de los datos
print("Mediana:", statistics.median(datos))#esto nos mostrara la mediana de los datos
print("Moda:", statistics.mode(datos))#esto nos mostrara la moda de los datos
print("Varianza:", statistics.variance(datos))#esto nos mostrara la varianza de los datos
print("Desviación estándar:", statistics.stdev(datos))#esto nos mostrara la desviacion estandar de los datos

# ..............................................................................................................................................

#  MÓDULO COLLECTIONS - Tipos de datos avanzados
import collections

print("\n🔹 MÓDULO COLLECTIONS")
contador = collections.Counter(["rojo", "azul", "rojo", "verde", "azul", "azul"])#esto nos mostrara la cantidad de veces que se repite cada elemento
print("Contador de elementos:", contador)

deque = collections.deque([1, 2, 3, 4, 5])#esto es una lista que se puede modificar por ejemplo se le puede agregar elementos al principio
print("Deque original:", deque)
deque.append(6)
print("Deque modificado:", deque)

# ..............................................................................................................................................

import json

# Abrir y leer el archivo JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Convertir JSON a diccionario

# Acceder a los valores
print("Nombre:", datos["nombre"])
print("Edad:", datos["edad"])
print("Email:", datos["email"])
print("Teléfonos:", ", ".join(datos["telefonos"]))


# Diccionario en Python
persona = {
    "nombre": "Ana Gómez",
    "edad": 25,
    "email": "ana@example.com",
    "activo": True
}

# Guardar en un archivo JSON
with open("persona.json", "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, indent=4)

print("JSON guardado en persona.json")

# ..............................................................................................................................................

#..........................................................................................................

#  MÓDULO RE - Expresiones regulares
import re

import re

def regex_notes():
    print("\n===== Expresiones Regulares en Python =====\n")
    
    # 1️⃣ Buscar la primera coincidencia con re.search()
    texto = "Mi número es 12345 y el de mi amigo es 67890."
    # Busca la primera secuencia de dígitos en el texto
    match = re.search(r"\d+", texto)
    if match:
        print("1️⃣ Primer número encontrado:", match.group())  # 12345
    
    # 2️⃣ Encontrar todas las coincidencias con re.findall()
    # Encuentra todas las secuencias de dígitos en el texto
    numeros = re.findall(r"\d+", texto)
    print("2️⃣ Todos los números encontrados:", numeros)  # ['12345', '67890']
    
    # 3️⃣ Verificar si un texto empieza con un patrón con re.match()
    frase = "Python es genial"
    # Comprueba si la frase empieza con "Python"
    if re.match(r"Python", frase):
        print("3️⃣ La frase empieza con 'Python'")
    
    # 4️⃣ Reemplazar coincidencias con re.sub()
    # Reemplaza los números en el texto con [NÚMERO]
    texto_modificado = re.sub(r"\d+", "[NÚMERO]", texto)
    print("4️⃣ Texto después de reemplazar números:", texto_modificado)
    
    # 5️⃣ Dividir texto con re.split()
    texto2 = "apple,banana;cherry orange"
    # Divide el texto usando comas, espacios y puntos y coma como separadores
    frutas = re.split(r"[ ,;]", texto2)
    print("5️⃣ Lista de palabras separadas:", frutas)
    
    # 6️⃣ Extraer un número de un log con re.search()
    log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
    # Busca un número dentro de corchetes en el log
    match_log = re.search(r"\[(\d+)\]", log)
    if match_log:
        print("6️⃣ ID del proceso extraído:", match_log.group(1))  # 12345
    
    # 7️⃣ Validar un email con RegEx
    email = "correo@example.com"
    # Patrón para validar correos electrónicos
    patron_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron_email, email):
        print("7️⃣ El email es válido")
    else:
        print("7️⃣ El email NO es válido")
    
    # 8️⃣ Caracteres especiales en RegEx
    print("\n===== Caracteres Especiales en RegEx =====")
    patrones = {
        "Cualquier carácter": r".",
        "Dígito (0-9)": r"\d",
        "No dígito": r"\D",
        "Caracter alfanumérico": r"\w",
        "No alfanumérico": r"\W",
        "Espacio en blanco": r"\s",
        "No espacio en blanco": r"\S",
        "Inicio de línea": r"^",
        "Fin de línea": r"$",
        "Grupo de caracteres": r"[aeiou]",  # Encuentra cualquier vocal
        "Grupo de captura": r"(\d+)",  # Captura un número
    }
    for descripcion, patron in patrones.items():
        print(f"- {descripcion}: {patron}")
    
    # 9️⃣ Cuantificadores en RegEx
    print("\n===== Cuantificadores en RegEx =====")
    cuantificadores = {
        "0 o más veces": r"ab*",  # Encuentra 'a', 'ab', 'abb', etc.
        "1 o más veces": r"ab+",  # Encuentra 'ab', 'abb', pero no 'a'
        "0 o 1 vez": r"ab?",  # Encuentra 'a' o 'ab'
        "Exactamente n veces": r"\d{4}",  # Encuentra números de 4 dígitos
        "Al menos n veces": r"\d{2,}",  # Encuentra números de al menos 2 dígitos
        "Entre n y m veces": r"\d{2,4}",  # Encuentra números de entre 2 y 4 dígitos
    }
    for descripcion, patron in cuantificadores.items():
        print(f"- {descripcion}: {patron}")

# Ejecutar las notas de RegEx
regex_notes()

texto = "hola mundo 123 AEIOU"

# 1️⃣ Cualquiera de los caracteres entre corchetes [aeiou]
print(re.findall(r"[aeiou]", texto))  
# Output: ['o', 'a', 'u', 'o']

# 2️⃣ Cualquier carácter excepto los indicados [^0-9]
print(re.findall(r"[^0-9]", texto))  
# Output: Lista con todos los caracteres excepto los números

# 3️⃣ Rango de caracteres minúsculas [a-zA-Z]
print(re.findall(r"[a-zA-Z]", texto))  
# Output: Lista con todas las letras

# 4️⃣ Rango de números [0-9]{2} (dos dígitos seguidos)
print(re.findall(r"[0-9]{2}", texto))  
# Output: ['12']

# ^...	Busca "Texto" solo si está al inicio de la cadena.
# [^...]	Encuentra cualquier carácter excepto "a", "b" o "c".
# 🔹 Buscar el primer carácter que NO sea una letra (a-z, A-Z)
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) 
# Output: <re.Match object; span=(4, 5), match=' '> (espacio en la posición 4)

# 🔹 Buscar el primer carácter que NO sea una letra o un espacio
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))  
# Output: <re.Match object; span=(30, 31), match='.'> (punto al final)


# 🔹 Buscar "cat" o "dog" en diferentes frases
print(re.search(r"cat|dog", "I like cats."))  
# Output: <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I love dogs!"))  
# Output: <re.Match object; span=(7, 10), match='dog'>

print(re.search(r"cat|dog", "I like both dogs and cats."))  
# Output: <re.Match object; span=(10, 13), match='dog'>

# 🔹 Encontrar todas las ocurrencias de "cat" o "dog" en la frase
print(re.findall(r"cat|dog", "I like both dogs and cats."))  
# Output: ['dog', 'cat']

# 🔹 Primera sección: Patrones "Py.*n" y "Py[a-z]*n"
test_cases_1 = [
    ("Pygmalion", r"Py.*n"),  # "Py", cualquier cosa en medio, y termina en "n" → Coincide: "Pygmalion"
    ("Python Programming", r"Py.*n"),  # Coincide: "Python Programmin" (hasta la última "n")
    ("Python Programming", r"Py[a-z]*n"),  # "Py", solo letras minúsculas en medio, y "n" → Coincide: "Python"
    ("Pyn", r"Py[a-z]*n")  # "Py", sin letras intermedias o minúsculas, y "n" → Coincide: "Pyn"
]

# 🔹 Segunda sección: Patrón "o+l+"
test_cases_2 = [
    ("goldfish", r"o+l+"),  # Busca "o" seguida de "l" → Coincide: "ol"
    ("woolly", r"o+l+"),  # Busca "o" seguida de "l" → Coincide: "ooll"
    ("boil", r"o+l+")  # "o" y "l" no están juntas → No coincide
]

import re  # Importamos la librería de expresiones regulares

# 🔹 Primera sección: ".com" vs "\.com"
print(re.search(r".com", "welcome"))  
# Output: <re.Match object; span=(2, 5), match='lco'>  
# 🛑 Aquí, "." significa "cualquier carácter", por lo que encuentra "lco" en "welcome".

print(re.search(r"\.com", "welcome"))  
# Output: None  
# 🔹 "\.com" busca literalmente ".com", pero "welcome" no lo contiene.

print(re.search(r"\.com", "mydomain.com"))  
# Output: <re.Match object; span=(8, 12), match='.com'>  
# ✅ Aquí ".com" aparece literalmente en "mydomain.com", por eso coincide.


# 🔹 Segunda sección: Uso de "\w*" (palabras)
print(re.search(r"\w*", "This is an example"))  
# Output: <re.Match object; span=(0, 4), match='This'>  
# ✅ "\w*" busca la primera palabra, que es "This" (se detiene en el primer espacio).

print(re.search(r"\w*", "And_this_is_another"))  
# Output: <re.Match object; span=(0, 20), match='And_this_is_another'>  
# ✅ Aquí, "\w*" coincide con todo el texto porque no hay espacios (los guiones bajos "_" cuentan como caracteres de palabra).


# ..............................................................................................................................................

# MÓDULO REQUESTS - Peticiones HTTP (requiere instalación: pip install requests)
# import requests
# print("\n🔹 MÓDULO REQUESTS")
# respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print("Respuesta HTTP:", respuesta.json())

# ..............................................................................................................................................
    #manejo de archivos "funciones"

#Leer un archivo línea por línea
# """with open('caperucita.txt', 'r') as file:
#     for lineas in file:
#         print(lineas.strip())"""

# #Leer todas las líneas en una lista
# """with open('caperucita.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)"""

# #Añadir texto
# """with open('caperucita.txt', 'a') as file:
#     file.write("\n\nBy:ChatGPT")"""

# #Sobreescribir el texto
# with open('caperucita.txt', 'w') as file:
#     file.write("\n\nBy:ChatGPT")


# ..............................................................................................................................................

# MÓDULO CSV - Manejo de archivos CSV
import csv

print("\n🔹 MÓDULO CSV")
with open("datos.csv", mode="w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)#esto nos creara un archivo csv usnado writer para escribir en el
    escritor.writerow(["Nombre", "Edad", "Ciudad"])#esto nos escribira en el archivo csv con writerow que escribe una fila
    escritor.writerow(["Juan", 30, "Madrid"])
    escritor.writerow(["Ana", 25, "Barcelona"])
print("Archivo CSV creado.")

# ..............................................................................................................................................

# MÓDULO UUID - Generación de identificadores únicos

import uuid

print("\n🔹 MÓDULO UUID")
print("UUID único generado:", uuid.uuid4())#esto nos generara un identificador unico

# ..............................................................................................................................................

# MÓDULO importlib 
#import  nombre del archivo
import importlib
modulo = importlib.reload#(nombre del alchivo)#esto nos importara el modulo

#nombre del archico.print_changes()#esto nos mostrara el cambio en el modulo 

    #reload()
    #vuelve a cargar el código actualizado sin necesidad de reiniciar Python.
#. ..............................................................................................................................................

#si ponemos from math import factorial importara solo la funcion factorial y si le ponemos as le asignara una variable

# ..............................................................................................................................................

#    📦 Paquetes en Python y sus Enfoques
# Los paquetes en Python permiten organizar el código en módulos reutilizables. Dependiendo del área de aplicación, hay paquetes específicos que se usan más en cada enfoque. Aquí te explico los más importantes en distintos campos.


# 1️⃣ Data Science y Análisis de Datos
    # 📊 ¿Qué es?
# Data Science se centra en la manipulación, análisis y visualización de datos para obtener información valiosa y tomar decisiones informadas.
    # 🛠️ Paquetes más usados
# NumPy → Para cálculos numéricos y matrices.
# Pandas → Para manejar datos en tablas tipo Excel.
# Matplotlib / Seaborn → Para visualizar datos con gráficos.
    # 📌 ¿Dónde se usa?
# Análisis financiero y de negocios.
# Estudio de tendencias en redes sociales.
# Investigación científica y académica.
# ..............................................................................................................................................
# 2️⃣ Machine Learning & Inteligencia Artificial
    # 🤖 ¿Qué es?
# Machine Learning permite que las computadoras aprendan de datos y hagan predicciones sin ser programadas explícitamente para cada tarea.
    # 🛠️ Paquetes más usados
# Scikit-learn → Modelos de ML clásicos como regresión, árboles de decisión, etc.
# TensorFlow / PyTorch → Redes neuronales y aprendizaje profundo.
    # 📌 ¿Dónde se usa?
# Predicción de precios en mercados financieros.
# Sistemas de recomendación (Netflix, Spotify).
# Diagnóstico médico asistido por IA.
# ..............................................................................................................................................
# 3️⃣ Ciberseguridad & Criptografía
    # 🛡️ ¿Qué es?
# La ciberseguridad protege datos y sistemas contra ataques y vulnerabilidades.
    # 🛠️ Paquetes más usados
# Hashlib → Para cifrar contraseñas y verificar integridad de datos.
# Cryptography → Para cifrado seguro de información.
# Socket → Para análisis de redes y escaneo de puertos.
    # 📌 ¿Dónde se usa?
# Protección de bases de datos y credenciales.
# Detección de intrusos en redes.
# Seguridad en transacciones bancarias.
# ..............................................................................................................................................
# 4️⃣ Desarrollo Web
    # 🌍 ¿Qué es?
# El desarrollo web permite construir aplicaciones accesibles desde navegadores.
    # 🛠️ Paquetes más usados
# Flask / Django → Frameworks para crear servidores web.
# Requests → Para interactuar con APIs y descargar datos.
# BeautifulSoup / Selenium → Para web scraping y automatización de navegación.
    # 📌 ¿Dónde se usa?
# Creación de plataformas y aplicaciones web.
# Extracción de datos de sitios web.
# APIs para integrar servicios de terceros.
# ..............................................................................................................................................
# 5️⃣ Automatización y Web Scraping
    # ⚙️ ¿Qué es?
# La automatización ayuda a realizar tareas repetitivas sin intervención humana, y el web scraping extrae información de páginas web.
    # 🛠️ Paquetes más usados
# Selenium → Para controlar navegadores automáticamente.
# BeautifulSoup → Para extraer información de páginas HTML.
# PyAutoGUI → Para automatizar acciones en la computadora.
    #  📌 ¿Dónde se usa?
# Llenado automático de formularios.
# Análisis de tendencias en sitios de noticias.
# Bots de automatización en redes sociales
# ..............................................................................................................................................
    # 📌 Resumen de Paquetes por Enfoque

# Data Science :	NumPy, Pandas, Matplotlib, Seaborn

# Machine Learning:	Scikit-learn, TensorFlow, PyTorch

# Ciberseguridad:	Hashlib, Cryptography, Socket

# Desarrollo Web:	Flask, Django, Requests, Selenium

# Automatización:	Selenium, BeautifulSoup, PyAutoGUI

#. ..............................................................................................................................................

    #  PRUEBAS
        #existen diferentes tipos de pruebas en python entre ellas(pruebas unitarias, pruebas de integracion,
        #pruebas de regresion, pruebas de humo, pruebas de aceptacion)
import unittest
#import #pytest
import sqlite3
import timeit

# --------------------------
# 🚀 FUNCIÓN PRINCIPAL A PROBAR
# --------------------------
def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b

# --------------------------
# 🧪 TEST UNITARIOS (Prueban funciones individuales)
# --------------------------
class TestSumar(unittest.TestCase):
    def test_suma_positivos(self):
        """Verifica la suma de números positivos"""
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativos(self):
        """Verifica la suma de números negativos"""
        self.assertEqual(sumar(-1, -1), -2)

    def test_suma_cero(self):
        """Verifica la suma con cero"""
        self.assertEqual(sumar(0, 5), 5)

# --------------------------
# 🔗 TEST DE INTEGRACIÓN (Verifica interacción entre módulos)
# --------------------------
def conectar_db():
    """Conecta a una base de datos en memoria (prueba)"""
    conn = sqlite3.connect(":memory:")
    return conn

def test_conexion():
    """Prueba si la conexión a la BD es exitosa"""
    conn = conectar_db()
    assert conn is not None  # La conexión debe existir

# --------------------------
# 🎭 TEST FUNCIONAL (Simula un caso real)
# --------------------------
# @pytest.mark.parametrize("a, b, esperado", [(2, 3, 5), (-1, -1, -2), (0, 5, 5)])
# def test_funcional_suma(a, b, esperado):
#     """Prueba la función sumar con distintos valores"""
#     assert sumar(a, b) == esperado

# --------------------------
# ⚡ TEST DE RENDIMIENTO (Mide la velocidad del código)
# --------------------------
def medir_tiempo():
    """Mide el tiempo de ejecución de la función"""
    tiempo = timeit.timeit("sumar(100, 200)", globals=globals(), number=10000)
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")

# --------------------------
# 🚀 EJECUTAR PRUEBAS
# --------------------------
# if __name__ == "__main__":
#     print("Ejecutando pruebas con unittest...")
#     unittest.main(exit=False)  # Ejecuta los test unitarios

#     print("\nEjecutando pruebas con pytest...")
#     pytest.main(["-q"])  # Ejecuta los test con pytest en modo silencioso

#     print("\nMidiendo rendimiento...")
#     medir_tiempo()  # Mide el tiempo de ejecución





