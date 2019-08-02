#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
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
print("##                                                                        ##");
print("##                       * Manejo de errores                              ##");
print("##                                                                        ##");
print("############################################################################");     
print("try:");
print("     cociente = dividendo / divisor");
print(" except:");
print('     print "No se permite la división por cero"');
print("#########################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# Ej 008_2
print("Inicio ej008_2");
try:
	maximo = int(input("ingrese la cantidad de numeros :"));
except:
	print ("ha ocurrio un Error. pero sigo von un valor = 10");
	maximo = 10
if maximo>0:
	def numeros_pares(maximo):
		contador = 1
		lista_de_pares=[]
		while contador<=maximo:
			lista_de_pares.append(contador*2);
			contador+=1
		return lista_de_pares
	print (numeros_pares(maximo));
print (input("Fin ej008_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_3
print("Inicio ej008_3 - ");
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");

import math
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_portenciacion(valor_1,valor_2):
	return valor_1**valor_2
def resultado_radicacion2(valor_1,valor_2):
	return  math.sqrt(valor_2);
def resultado_porcentage(valor_1,valor_2):
	return valor_1/valor_2*100
def resultado_cociente(valor_1,valor_2):
	return valor_1//valor_2
def resultado_resto(valor_1,valor_2):
	return valor_1%valor_2

print ("resultado suma : "+str(resultado_suma(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto(valor1,valor2)));
print (input("Fin ej008_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_4
print("Inicio ej008_4 - manejo errores");
from AGT_Ej_009_Metodo import *
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)));
print (input("Fin ej008_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_5
print("Inicio ej008_5- manejo errores");

variable = "variable original"
def variable_global():
	print ("INGERSO A LA FUNCION")
	global variable1
	variable = "variable global modificada desde dentro de una funcion"

print ("variable original: ",end=(""))
print (variable)
variable_global()
print ("variable global modificada: ",end=(""))
print (variable)
print (input("Fin ej008_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_6
print("Inicio ej008_6 - manejo derrores");
try:
	x = 10
	y = 0
	print(x/y)
except Exception as e:
	print("Exeception occured:{}".format(e))
finally:
	x = 10
	y = 2
	print(x/y)
print ("continuo")
print ("continuo")
print ("continuo")

print (input("Fin ej008_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_7
print("Inicio ej008_7 - manejo derrores");
#try:
    # aquí ponemos el código que puede lanzar excepciones
#except:
    # ERROR de sintaxis, esta sentencia no puede estar aquí,
    # sino que debería estar luego del except IOError.
#except IOError:
    # Manejo de la excepción de entrada/salida
print (input("Fin ej008_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_8
print("Inicio ej008_8 - manejo derrores");
#try:
#    archivo = open("miarchivo.txt")
    # procesar el archivo
#except IOError:
#    print "Error de entrada/salida."
    # realizar procesamiento adicional
#except:
    # procesar la excepción
#finally:
    # si el archivo no está cerrado hay que cerrarlo
#    if not(archivo.closed):
#        archivo.close()
print (input("Fin ej008_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_9
#print("Inicio ej008_9 - manejo derrores");
lista = [10, 100, 1000, 10000]
iterador = iter(lista)
try:
    while True:
        print(iterador.__next__())        
except StopIteration:
    print("Se ha alcanzado el final de la lista")
