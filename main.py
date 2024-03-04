from colorama import Fore, Back, Style
import Clases.Pelicula as peli
import time as t
import graphviz as gv
 
# --- Varrables globales ---
archivo = ""
contenido = None
lista_peliculas = []
lista_actores = []

def cambioColor(color, texto):
    if color == 1:  # Verde 
        print("\033[1;32;40m" + texto + "\033[m")
    elif color == 2:  # Rojo
        print("\033[1;31;40m" + texto + "\033[m")
    else:
        print("Color no válido")

def mostrar_informacion_desarrollador():
    print("="*50)
    print("Bienvenido al Sistema       ")
    print("Desarrollado por:           ")
    print("Lenguajes Formales y de Programación")
    print("Seccion: B+")
    print("Carné: 202200196")
    print("Nombre: Gerardo Leonel Ortiz Tobar")
    print("="*50)
    input("Presiona cualquier tecla para continuar...")
    mostrar_menu_principal()

def validar_archivo(nombre_archivo):
    if not nombre_archivo:
        return False
    return True



def mostrar_menu_principal():
    global archivo, contenido
    print("===================================")
    print("           Menú Principal          ")
    print("===================================")
    print("1. Cargar archivo de entrada")
    print("2. Gestionar películas")
    print("3. Filtrado")
    print("4. Gráficas")
    print("5. Salir")
    print("")
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        limpiar_variables()
        archivo = input("Ingrese el nombre del archivo de entrada: ")
        contenido = cargar_archivo_entrada(archivo + ".lfp")
        agregarPeliculas()
        t.sleep(0.1)
        
    elif opcion == '2':
        print(archivo)
        if validar_archivo(archivo):
         opcion_gestion_peliculas()
        else:
            cambioColor(2,"No se ha cargado un archivo de entrada")
        
    elif opcion == '3':
        if validar_archivo(archivo):
            opcion_filtrado()
        else:
            cambioColor(2,"No se ha cargado un archivo de entrada")
        
    elif opcion == '4':
        if validar_archivo(archivo):
            generar_grafico_peliculas()
        else:
            cambioColor(2,"No se ha cargado un archivo de entrada")
        
    elif opcion == '5':
        cambioColor(1,"Gracias por utilizar el sistema :)")
        exit()
    else:
        cambioColor(2,"Opción inválida")
    mostrar_menu_principal()


def cargar_archivo_entrada(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

            return contenido
        
    except FileNotFoundError:
        cambioColor(2,f"El archivo '{nombre_archivo}' no se encontró.")
        return None
    except Exception as e:
        cambioColor(2,f"Ocurrió un error al leer el archivo '{nombre_archivo}': {e}")
        return None
    

def agregarPeliculas():
    global contenido
    if contenido == None:
        cambioColor(2,"No se ha cargado un archivo de entrada.")
        return
    else:
        for i in contenido:
            cadena = i.split(';')
            nombre = cadena[0]
            actores = cadena[1].split(',')
            year = cadena[2].strip()
            genero = cadena[3].strip()
            pelicula = peli.Pelicula(nombre, year, genero)
            eliminar_pelicula(nombre)
            lista_peliculas.append(pelicula)
            for j in actores:
                actor = j.strip()
                pelicula.agregar_actor(actor)
                if actor not in lista_actores: 
                    lista_actores.append(actor)
        cambioColor(1,"Peliculas agregadas correctamente")

def mostrarActores_filtro():
    contador = 0
    print("===================================")
    print("         Mostrar Actores           ")
    print("===================================")
    
    in_actor = input("Ingrese el nombre del actor: ")

    filtrar_por_actor(in_actor)


def filtrar_por_actor(actor_elegido):
    contador = 0
    print("===================================")
    print("        Peliculas por actor        ")
    print("===================================")
    for i in lista_peliculas:
        aux_actores = i.get_actores()
        if actor_elegido in aux_actores:
            print(i.get_nombre())
            contador += 1
    if contador == 0:
        print("No hay películas registradas con ese actor")

def opcion_filtrado_por_año(opcion_year):
    contador = 0
    print("===================================")
    print("        Peliculas por año          ")
    print("===================================")
    t.sleep(2)
    for i in lista_peliculas:
        if i.get_year() == opcion_year:
            contador += 1
            print(f"{contador}-{i.get_nombre()}-{i.get_genero()}")
    if contador == 0:
        print("No hay películas registradas en ese año")

def opcion_filtrado_por_genero(opcion_genero):
    contador = 0
    print("===================================")
    print("        Peliculas por género        ")
    print("===================================")
    t.sleep(2)
    for i in lista_peliculas:
        if i.get_genero() == opcion_genero:
            print(i.get_nombre())
            contador += 1
    if contador == 0:
        print("No hay películas registradas con ese género")

def mostrar_peliculas():
    contador = 0
    print("===================================")
    print("        Mostrar Películas          ")
    print("===================================")
    t.sleep(2)
    for i in lista_peliculas:
        contador += 1
        nombre = i.mostrarPelicula()
        print(f"{contador}-{nombre}")

def mostrarActores(pelicula_elegida):
    print("===================================")
    print("        Mostrar Actores          ")
    print("===================================")
    t.sleep(2)
    print(f"Nombre: {lista_peliculas[pelicula_elegida-1].get_nombre()}")
    actores = lista_peliculas[pelicula_elegida-1].get_actores()
    if len(actores) == 0:
        print("No hay actores registrados")
        return
    actores_str = ", ".join(actores)
    print(f"Actores: {actores_str}")

def opcion_gestion_peliculas():
    while True:
        print("===================================")
        print("        Menu de Películas          ")
        print("===================================")
        print("1. Mostrar películas")
        print("2. Mostrar actores")
        print("3. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            t.sleep(2)
            mostrar_peliculas()
        elif opcion == '2':
            mostrar_peliculas()
            pelicula_elegida = int(input("Selecciona una película: "))
            t.sleep(2)
            mostrarActores(pelicula_elegida)
        elif opcion == '3':
            t.sleep(2)
            return  
        else:
            cambioColor("Opción inválida")

def opcion_filtrado():
    while True:
        print("===================================")
        print("        Menu de  Filtrado          ")
        print("===================================")
        print("1. Filtrar por actor")
        print("2. Filtrar por año")
        print("3. Filtrar por género")
        print("4. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrarActores_filtro()
            
        elif opcion == '2':
            opcion_year = input("Ingrese el año: ")
            opcion_filtrado_por_año(opcion_year)
            t.sleep(2)
            
        elif opcion == '3':
            opcion_genero = input("Ingrese el género: ")
            opcion_filtrado_por_genero(opcion_genero)
            t.sleep(2)
            
        elif opcion == '4':
            return 
        
def eliminar_pelicula(nombre_pelicula):
    global lista_peliculas
    for pelicula in lista_peliculas:
        if pelicula.get_nombre() == nombre_pelicula:
            lista_peliculas.remove(pelicula)
            cambioColor(2,f"La película '{nombre_pelicula}' ha sido eliminada con éxito.")
            return
    
def limpiar_variables():
    global archivo, contenido, lista_peliculas, lista_actores
    archivo = ""
    contenido = None
    lista_peliculas = []
    lista_actores = []

def generar_grafico_peliculas():
    global lista_peliculas, lista_actores
    grafo = gv.Digraph(format='png')

    for pelicula in lista_peliculas:
        etiqueta = f'<<table border="0" cellborder="1" cellspacing="0">' \
                  f'<tr><td colspan="1" bgcolor="lightgrey"><b>{pelicula.get_nombre()}</b></td></tr>' \
                  f'<tr><td>{pelicula.get_year()}</td></tr>' \
                  f'<tr><td>{pelicula.get_genero()}</td></tr>' \
                  f'</table>>'
        grafo.node(pelicula.get_nombre(), shape='plaintext', label=etiqueta)

    for actor in lista_actores:
        grafo.node(actor, shape='circle', color='black')

    for pelicula in lista_peliculas:
        actores_pelicula = pelicula.get_actores()
        for actor in actores_pelicula:
            grafo.edge(actor, pelicula.get_nombre()) 

    grafo.render('peliculas', view=True)
    print("Gráfico de películas generado con éxito.")


mostrar_informacion_desarrollador()
