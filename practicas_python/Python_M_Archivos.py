#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 1 -¿Qué es Python?                                         ##");
print("##            * Instalación y configuración                               ##");
print("##            * Errores sintácticos y lógicos                             ##");
print("##            * Programación secuencial                                   ##");
print("##            * Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            * Estructuras repetitivas                                   ##");
print("##                                                                        ##");
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            * Tipos de variables                                        ##");
print("##            * Procesamiento de cadenas                                  ##");
print("##            * Listas                                                    ##");
print("##            * Diccionarios                                              ##");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            * Parámetros                                                ##");
print("##            * Retorno de datos                                          ##");
print("##            * Return de listas                                          ##");
print("##            * Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##");
print("##         Listas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer listas                                           ##");
print("##         Tuplas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer Tuplas                                           ##");
print("##         Diccionarios                                                   ##");
print("##            * Funcionamiento de diccionarios                            ##");
print("##            * Estructuras tipo JSON                                     ##");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * Cursor y verificación de consultas                        ##");
print("##            * Manejo de errores                                         ##");
print("##                                                                        ##");
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Modulo time, datetime                                     ##");
print("##            * Manejo de fechas y horas                                  ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("##         Unidad 8 - OPEN CV                                             ##");
print("##            * Procesamiento de imágenes en OpenCV                       ##");
print("##            * Detección y descripción de imágenes                       ##");
print("##            * Detección de objetos                                      ##");
print("##                                                                        ##");
print("##         Unidad 9 - Programación de eventos                             ##");
print("##            * Módulo sched                                              ##");
print("##            * Declaración de programadores                              ##");
print("##            * Programar eventos y poner en marcha el programador        ##");
print("##            * Programación de eventos considerando prioridades          ##");
print("##            * Cancelación de eventos                                    ##");
print("##                                                                        ##");
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");#print("https://www.w3schools.in/python-tutorial/gui-programming/")
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("############################################################################");
print("##                                                                        ##");
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Modulo time, datetime                                     ##");
print("##            * Manejo de fechas y horas                                  ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("############################################################################");     
print("##                                                                        ##");
print("##                                archivar                                ##")
print("##                                                                        ##");
print("############################################################################");
# Ej 009_4
print("Inicio ej 009_4 - manejo desde un archivo separado")
from AGT_Ej_009_Metodo import *
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "))
		valor2=float(input("valor 2 : "))
		break
	except ValueError:
		print("Error. solo nomeros")
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)))
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)))
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)))
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)))
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)))
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)))
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)))
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)))
print (input("ej 009-1        continuar?"));
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

pantalla_1_raiz=Tk()#                                Define la ventana principal de la aplicación
pantalla_1_raiz.title("Mi primer pantalla")#         ancho   x alto
pantalla_1_raiz.geometry("640x480")#                 Define las dimensiones de la ventana, que se ubicará en el centro de la pantalla. Si se omite esta línea la # ventana se adaptará a los widgets que se coloquen en ella. 
pantalla_1_raiz.configure(bg = "blue")#				 Asigna un color de fondo a la ventana.
#ttk.Button(pantalla_1_raiz, text='Exit', command=quit).pack(side=BOTTOM)
#pantalla_1_raiz.iconbitmap("icono.png")
#frame1_pantalla_1_raiz(pantalla_1_raiz)

# Define un botón en la parte inferior de la ventana que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'pantalla_1_raiz' donde se ubicará el botón
pantalla_1_raiz.mainloop()

