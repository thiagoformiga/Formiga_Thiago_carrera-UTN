import pygame
from color import * 

def cargar_imagen(ruta_acceso,surface,tamaño:tuple,posicion:list):
    """
    descripcion:esta carga, escala y blitea una imagen ademas retorna su rectangulo
    parametros:la ruta, donde se bliteara, el tamaño y la posicion
    retorno:
    """
    #crear/cargar imagen
    imagen = pygame.image.load(ruta_acceso)
    imagen = pygame.transform.scale(imagen,tamaño)
    surface.blit(imagen,posicion)
    return imagen.get_rect()

#left --> a cuanto de la izquierda quiero que este
#top --> a cuanto de la arriba quiero que este
# left --> a cuanto de la derecha quiero que este
# left --> a cuanto de la abajo quiero que este
def crear_rectangulo_pantalla(surface,color:str,left_x:int,top_y:int,widht_Ancho:int,height_alto:int)->pygame.rect:
    """
    descripcion: esta funcion dibuja y devuelve la posicion de un rectangulo
    parametros: la superficie donde lo hagamos,el color,pos_x,pox_y,donde lo dibujamos y el largo y el ancho que le daremos al rectangulo
    retorno: retorna las dimensiones del rectangulo
    """
    surface_rectangulo = pygame.Rect(left_x,top_y,widht_Ancho,height_alto)#creo la superficie del rectangulo
    pygame.draw.rect(surface,color,surface_rectangulo,border_radius=15)#dibujo el rectangulo
    return surface_rectangulo


def crear_texto_pantalla(surface,texto:str,color_texto:str,texto_cordenadas:tuple,fuente:str,tamaño_letra:int):
    """
    descripcion:esta funcion renderiza y blitea un texto a pantalla
    parametros:la superficie,el color,las cordenadas(tupla)
    retorno:no retorna nada
    """
    fuente = pygame.font.SysFont(fuente,tamaño_letra)
    texto_renderizado = fuente.render(texto,True,color_texto)
    surface.blit(texto_renderizado,texto_cordenadas)

def crear_boton_texto(surface,color_boton,left_x:int,top_y:int,widht_Ancho:int,height_alto:int,texto_boton:str,color_texto,posicion_texto:tuple,fuente:str,tamaño_letra:int):
    """
    descripcion:esta funcion crea un boton con su texto en pantalla
    parametros: la superficie, la posx,posy,el largo y el ancho que le daremos al boton ademas el texto que escribimos en el 
    retorna una surface
    """
    surface_boton = crear_rectangulo_pantalla(surface, color_boton, left_x, top_y, widht_Ancho, height_alto)
    crear_texto_pantalla(surface, texto_boton, color_texto,posicion_texto,fuente,tamaño_letra)
    return surface_boton

def verificar_apreto(surface,pos_apreto:tuple)->bool:
    """
    descripcion:esta funcion recibe una superficie y las cordenadas donde se apreto, para verificar si hubo una colicion dentro de la superficie
    parametros:recibe la superficie y la pos donde apreto
    retorno: retorna un bool 
    """
    return surface.collidepoint(pos_apreto)


def verificar_colission(rect1,rect2)->bool:
    """
    descripcion:verifica la colision entre rectangulos
    parametros:recibe ambos rectangulos
    retorno:retorna un bool
    """
    colision = rect1.colliderect(rect2)
    return colision


def mostrar_texto(surface,lista,indice,color,posicion):
    """
    descripcion:esta funcion escribe en pantalla un texto de una lista 
    parametros:recibe la lista, indice, color,posicion y lugar donde lo blitea
    retorno:no retorna nada
    """
    texto = lista[indice]
    crear_texto_pantalla(surface,texto,color,posicion,"Arial",25)

def mostrar_score(surface,score:int)->int:
    """
    descripcion:esta funcion muestra el score y lo blitea en pantalla
    parametros:recibe los parametros y donde lo va a blitear
    retorno:retorna el score
    """
    texto = f"Puntaje: {score}"
    crear_texto_pantalla(surface,str(texto),BLACK,(20,253),"Arial",30)
    return score















def crear_rectangulos_movimiento(surface_pantalla):
    #rectangulos de movimiento

    crear_rectangulo_pantalla(surface_pantalla,NARANJA_OSCURO,150,350,80,50)
    crear_rectangulo_pantalla(surface_pantalla,VERDE_CLARO,235,350,80,50)
    crear_rectangulo_pantalla(surface_pantalla,AMARILLO,320,350,80,50)
    crear_rectangulo_pantalla(surface_pantalla,AZULCLARO,405,350,80,50)
    crear_rectangulo_pantalla(surface_pantalla,ROJO,490,350,80,50)
    crear_boton_texto(surface_pantalla,VIOLETA,575,350,80,50,"Avanza 1",BLACK,(580,355),"Arial",20)
    crear_rectangulo_pantalla(surface_pantalla,AMARILLO,660,350,80,50)
    crear_rectangulo_pantalla(surface_pantalla,GREEN3,745,350,80,50)

    crear_rectangulo_pantalla(surface_pantalla,NARANJA_OSCURO,150,450,80,50)
    crear_rectangulo_pantalla(surface_pantalla,VERDE_CLARO,235,450,80,50)
    crear_rectangulo_pantalla(surface_pantalla,AMARILLO,320,450,80,50)
    crear_boton_texto(surface_pantalla,AZULCLARO,405,450,80,50,"Retrocede",BLACK,(405,450),"Arial",20)
    crear_texto_pantalla(surface_pantalla,"1",BLACK,(437,470),"Arial",20)
    crear_rectangulo_pantalla(surface_pantalla,ROJO,490,450,80,50)
    crear_rectangulo_pantalla(surface_pantalla,VIOLETA,575,450,80,50)
    crear_rectangulo_pantalla(surface_pantalla,AMARILLO,660,450,80,50)
    crear_rectangulo_pantalla(surface_pantalla,GREEN3,745,450,80,50)

