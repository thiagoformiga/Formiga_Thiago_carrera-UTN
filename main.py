import pygame
from color import * 
from funciones_pantalla import *
from funciones_datos import *
from datos import *

#Iniciamos pygame
pygame.init()
######################################################################################################
#Creacion de la pantalla
#Tamaño pantalla
PANTALLA_ALTO = 670
PANTALLA_ANCHO = 900
TAMANO_PANTALLA = (PANTALLA_ANCHO,PANTALLA_ALTO)
surface_pantalla = pygame.display.set_mode(TAMANO_PANTALLA)
#Titulo ventana
pygame.display.set_caption('Carrera UTN')
######################################################################################################
#Botones para apretar
surface_boton_comenzar = crear_boton_texto(surface_pantalla,AZULCLARO,152,568,300,80,"Comenzar",BLACK,(185,590),"impact",50)
surface_boton_terminar = crear_boton_texto(surface_pantalla,AZULCLARO,430,568,270,80,"Terminar",BLACK,(450,570),"impact",50)

surface_boton_a = crear_boton_texto(surface_pantalla,ROJO,263,180,30,30,"a",AMARILLO,(270,185),"Arial",20)
surface_boton_b = crear_boton_texto(surface_pantalla,ROJO,480,180,30,30,"b",AMARILLO,(490,185),"Arial",20)
surface_boton_c= crear_boton_texto(surface_pantalla,ROJO,700,180,30,30,"c",AMARILLO,(710,185),"Arial",20)
######################################################################################################
#Timer
timer_segundos = pygame.USEREVENT
#Seteo el timer para que me muestre de a un segundo
pygame.time.set_timer(timer_segundos,1000)
segundos = 5
fin_tiempo = False
#############################################################################################################
#creacion listas
lista_preguntas = crear_sublistas(lista,"pregunta")
lista_opcion_a = crear_sublistas(lista,"a")
lista_opcion_b = crear_sublistas(lista,"b")
lista_opcion_c = crear_sublistas(lista,"c")
lista_opcion_correcta = crear_sublistas(lista,"correcta")
lista_temas = crear_sublistas(lista,"tema")
#contador para el indice de las listas
contador_indice = 0
##################################################################################################################
#Cuadro para guardar nombre
ingreso_nombre = ""
rectangulo_texto =crear_rectangulo_pantalla(surface_pantalla,BLANCO,250,250,400,50)

#boton para salir mostrar
sruface_boton_salir = crear_boton_texto(surface_pantalla,AZULCLARO,700,568,300,80,"SALIR",BLACK,(710,573),"impact",30)
#################################################################################################################
#imagen_alumno
posicion_inicial = [80,350]
posicion_x_alumno = posicion_inicial[0]
posicion_y_alumno = posicion_inicial[1]
alumno_rect = pygame.Rect(50,50,posicion_x_alumno,posicion_y_alumno)
bandera_fila_arriba = True
bandera_fila_abajo = False

#Botones con los cuale colisionara el personaje
surface_avanza_uno =crear_boton_texto(surface_pantalla,VIOLETA,575,350,80,50,"Avanza 1",BLACK,(580,355),"Arial",20)
bandera_avanza_uno = False
surface_retrocede_uno = crear_boton_texto(surface_pantalla,AZULCLARO,405,450,80,50,"Retrocede",BLACK,(405,450),"Arial",10)
bandera_retrocede_uno = False
#################################################################################################



#imagen llegada
imagen_llegada = cargar_imagen("utn_llegada.png",surface_pantalla,(80,50),[65,320])
#llego al final
bandera_finalizo = False
ingreso_usuario = False
llego_a_meta = False






#para validar las respuestas
respuesta_correcta = False
respuesta_incorrecta = False
score = 0


#para el boton de comenzar
comenzar= False
correr = True
posicion = [0,0]
while correr:
    surface_pantalla.fill(AZULREAL)
    #imagen carrera 
    cargar_imagen("zimagen_carrera_utn.png",surface_pantalla,(250,200),[0,0])
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        #si apreto las teclas siempre y cuando aprete terminar o haya llegado al final
        
        #dejo de mostrar las preguntas
        if bandera_finalizo:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:#poder utilizar la key de borrar porque sino muestra un caracter vacio
                    ingreso_nombre = ingreso_nombre[0 :-1]
                else:
                    ingreso_nombre += evento.unicode 
                #SI APRETO SHIFT A LA DERECHA INGRESO EL USUARIO
                if evento.key == pygame.K_RSHIFT:
                    crear_json_usuario_score(ingreso_nombre, score, "puntaje_usuarios.json")
                    ingreso_usuario = True
                    ingreso_nombre = ""  # Reiniciar ingreso después
            
        if evento.type == pygame.USEREVENT:
            #sete un clock 
            # el cual cuenta hasta 5 si se pasa de cinco simplemente salta a la siguiente pregunta
            if evento.type == timer_segundos and comenzar:
                segundos -= 1
                if segundos == 0:
                    fin_tiempo = True

                if fin_tiempo == True:
                    fin_tiempo = False
                    contador_indice += 1
                    segundos = 5
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion = list(evento.pos)
            print(posicion)
            if verificar_apreto(surface_boton_comenzar,posicion):
                comenzar = True
                segundos = 5
                contador_indice = 0
                score = 0
                respuesta_correcta = False
                respuesta_incorrecta = False
                bandera_finalizo = False
                posicion_x_alumno = 80
                posicion_y_alumno = 350
                bandera_fila_abajo =False
                bandera_fila_arriba = True
                llego_a_meta =False
                moviendo =False
            
            if comenzar:
                #verificar la respuesta y me devuelve un bool
                if verificar_apreto(surface_boton_a,posicion):
                    if "a" == lista_opcion_correcta[contador_indice]:
                        respuesta_correcta = True
                    else:
                        respuesta_incorrecta = True
                elif verificar_apreto(surface_boton_b,posicion):
                    if "b" == lista_opcion_correcta[contador_indice]:
                        respuesta_correcta = True
                    else:
                        respuesta_incorrecta = True
                elif verificar_apreto(surface_boton_c,posicion):
                    if "c" == lista_opcion_correcta[contador_indice]:
                        respuesta_correcta = True
                    else:
                        respuesta_incorrecta = True

            if verificar_apreto(surface_boton_terminar,posicion):
                bandera_finalizo = True
                llego_a_meta = False
                comenzar = False
            if verificar_apreto(sruface_boton_salir,posicion):
                ingreso_usuario = False
        
    if respuesta_correcta:
        score += 10
        segundos = 5
        contador_indice += 1
    
    if respuesta_incorrecta:
        segundos = 5
        contador_indice += 1

    if bandera_fila_arriba:
        if respuesta_correcta:
            posicion_x_alumno += 170
        if respuesta_incorrecta:
            posicion_x_alumno -= 90
    if bandera_fila_abajo:
        if respuesta_correcta:
            posicion_x_alumno -= 170
        if respuesta_incorrecta:
            posicion_x_alumno  += 90

    alumno_rect = pygame.Rect(50,50,posicion_x_alumno,posicion_y_alumno)
    if posicion_x_alumno < 80:
        posicion_x_alumno = 80
    #para cuando se vaya del final de la fila de arriba
    if posicion_x_alumno>800 and bandera_fila_arriba:
        posicion_y_alumno = 450
        posicion_x_alumno = 770
        bandera_fila_arriba = False
        bandera_fila_abajo = True   
    #para cuando se vaya del final de la fila de arriba
    if posicion_x_alumno>790 and bandera_fila_abajo:
        bandera_fila_arriba = True
        bandera_fila_abajo = False
        posicion_y_alumno = 350
        posicion_x_alumno = 770
    #avanza uno
    if posicion_x_alumno > 545 and posicion_x_alumno<658 and posicion_y_alumno>345 and posicion_y_alumno<400 and  bandera_avanza_uno == False:
        posicion_x_alumno += 95
        bandera_avanza_uno = True
    #retrocede uno
    if posicion_x_alumno > 405 and posicion_x_alumno<455 and posicion_y_alumno>410 and  posicion_y_alumno<500 and  bandera_retrocede_uno == False:
        if respuesta_correcta:
            print("retrocede uno")
            posicion_x_alumno += 160
        bandera_retrocede_uno = True
    #en caso de que llegue al final
    if posicion_x_alumno < 140 and bandera_fila_abajo:
        bandera_finalizo = True
        llego_a_meta = False
        comenzar = False

    respuesta_incorrecta = False
    respuesta_correcta = False  

    if contador_indice < len(lista_preguntas):
        pass
    else:
        contador_indice = 0
    #bliteo las listas
    if comenzar:
        #flecha de dar vuelta
        cargar_imagen("zflecha_curva.png",surface_pantalla,(100,100),[800,372])
        #imagen_llegada
        cargar_imagen("utn_llegada.png",surface_pantalla,(80,50),[50,450])
        #rectangulo donde van las preguntas , respuesta
        crear_rectangulo_pantalla(surface_pantalla,VERDE_OSCURO,260,0,630,300)
        #botones respuestas
        crear_boton_texto(surface_pantalla,ROJO,263,180,30,30,"a",AMARILLO,(270,185),"Arial",20)
        crear_boton_texto(surface_pantalla,ROJO,480,180,30,30,"b",AMARILLO,(490,185),"Arial",20)
        crear_boton_texto(surface_pantalla,ROJO,700,180,30,30,"c",AMARILLO,(710,185),"Arial",20)
        ###segundos
        crear_texto_pantalla(surface_pantalla,f"Segundos: {str(segundos)}",BLACK,(20,200),"Arial",30)
        ##score
        mostrar_score(surface_pantalla,score)
        #preguntas y respuestas
        mostrar_texto(surface_pantalla,lista_preguntas,contador_indice,AMARILLO_CREMA,(274,20))
        mostrar_texto(surface_pantalla,lista_opcion_a,contador_indice,AMARILLO_CREMA,(263,139))
        mostrar_texto(surface_pantalla,lista_opcion_b,contador_indice,AMARILLO_CREMA,(480,139))
        mostrar_texto(surface_pantalla,lista_opcion_c,contador_indice,AMARILLO_CREMA,(700,139))
        #cuadrados del movimiento
        crear_rectangulos_movimiento(surface_pantalla)
        #imagen personaje
        crear_texto_pantalla(surface_pantalla,"SAlIDA",BLACK,(75,360),"Arial",30)
        cargar_imagen("zalumno.png",surface_pantalla,(50,50),[posicion_x_alumno,posicion_y_alumno])
    
    if bandera_finalizo and ingreso_usuario != True:
        crear_texto_pantalla(surface_pantalla,"Carga tu nombre(shift derecho para guardar)",BLACK,(356,84),"Arial",30)
        crear_rectangulo_pantalla(surface_pantalla,BLANCO,250,250,400,50)
        texto =crear_texto_pantalla(surface_pantalla,ingreso_nombre,BLACK,(255,255),"Arial",30)

    if ingreso_usuario and comenzar != True :
        bandera_finalizo = False
        crear_boton_texto(surface_pantalla,AZULCLARO,700,568,300,80,"SALIR",BLACK,(710,573),"impact",30)
        leer_puntajes(surface_pantalla,"puntaje_usuarios.json")


    if ingreso_usuario == False:
        #boton terminar
        crear_boton_texto(surface_pantalla,AZULCLARO,152,568,270,80,"Comenzar",BLACK,(185,570),"impact",50)
        crear_boton_texto(surface_pantalla,AZULCLARO,430,568,270,80,"Terminar",BLACK,(470,570),"impact",50)
    pygame.display.flip()

pygame.quit()
