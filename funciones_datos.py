from datos import *
from funciones_pantalla import*
from color import * 



def crear_sublistas(lista_princ:list,clave:str):
    sublista = []
    for diccionario in lista_princ:
        sublista.append(diccionario[clave])
    return sublista


def crear_json_usuario_score(nombre:str,score:str,nombre_archivo:str):
    """
    descripcion: esta funcion verifica si existe un archiv json si lo encuentra lo lee y le carga los datos que ya tiene escritos sino crea un json y le carga los datos
    parametros: recibe el nombre ingresado, el score , nombre que le dara al archivo
    retorno : no retorna nada
    """
    import json
    import os

    nuevo_usuario_ingresado = {'nombre': nombre, 'score': score}
    # en caso de existir el archivo carga los nombres y scores que ya existian
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            puntajes = json.load(archivo)
    else:
        puntajes = []
    
    #agrega nombres y scores a la lista
    puntajes.append(nuevo_usuario_ingresado)
    
    #guardo en el archivo con los nuevos datos ingresados
    with open(nombre_archivo, 'w') as archivo:
        json.dump(puntajes, archivo, indent=4)

def leer_puntajes(surface,nombre_archivo='puntajes.json'):
    """
    descripcion:esta funcion lee un archivo json si existe sino devuelve una excepcion ademas con esta funcion ordeno puntajes y los bliteo a pantalla
    parametros:la surface, nombre del archivo
    retorno:
    """
    import json
    try:
        #intenta leer el json
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de puntajes.")
        return
    except json.JSONDecodeError:
        print("El archivo de puntajes está vacío o está corrupto.")
        return
    
    # ordeno a los puntajes de menor a mayor
    puntajes_ordenados = ordenar_puntaje_mayores(datos, 'score')
    mostrar_puntaje(surface,puntajes_ordenados,"score","nombre")



def ordenar_puntaje_mayores(lista,clave):
    """
    descripcion:esta funcion oredena una lista por la clave de manera ascendente 
    parametros:recibe la lista y la clave
    retorno:retorna la lista ordenada
    """
    return sorted(lista, key=lambda x: x[clave], reverse=True)

def mostrar_puntaje(surface,lista,clave_score,clave_nombre):
    """
    descripcion:esta funcion recore una lista y bliteo los textos de sus datos
    parametros:recibe la surface, la lista , las clave de los datos
    retorno:
    """
    crear_texto_pantalla(surface,"puntajes",BLACK,(379,-15),"Arial",80)
    posicion_y = 50
    for i in range(len(lista)):
        if i < 10:
            posicion_y += 40
            datos = lista[i]
            texto = f"{datos[clave_nombre]}: {datos[clave_score]}"
            crear_texto_pantalla(surface,texto,BLACK,(379,posicion_y),"Arial",30)