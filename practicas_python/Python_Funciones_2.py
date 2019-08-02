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
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            * Parámetros                                                ##");
print("##            * Retorno de datos                                          ##");
print("##            * Return de listas                                          ##");
print("##            * Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones y Metodos                            ##");
print("##                         -------------------                            ##");
print("##                                                                        ##");
print("##     Funciones    Description                                           ##");
print("##              lambda                                                    ##");
print("##                                                                        ##");
print("##                                                                        ##");
print("##     Metodos son finciones dentro de clases donde se deberia instanciar ##");
print("##              a la clase con self                                       ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones,  Metodos                            ##");
print("##                                                                        ##");
print("##                             y Generadores                              ##");
print("##                                                                        ##");
print("############################################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#print(input("continuar?"));
print("https://www.w3schools.com/python/python_ref_list.asp");
print("\nhttps://www.w3schools.com/python/python_lists.asp");
print("https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html")
print("https://python-para-impacientes.blogspot.com/2014/02/funciones.html")
print("Inicio ej 002_3_1 ");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones,  Metodos                            ##");
print("##                                                                        ##");
print("############################################################################");


#                          como funcion
def funcion (var_1, var_2):
	return (var_1 *var_2)
print (funcion (2,4))
mi_array=(3,6)
print (funcion (*mi_array))# ver el "*"
#                          como Metodo
class Clase1:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)
ej=Clase1()
ej.metodo(6,5)
print (ej.resultado)



print (input("Fin ej 002_3_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_2
print("Inicio ej 002_3_2 ");
print("############################################################################");
print("##                                                                        ##");
print("##                                Metodos                                 ##");
print("##                                                                        ##");
print("############################################################################");
class Clase2:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def __init__(self):#construye los objetos
		self.var_1=  0
		self.var_2=  0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)

ej=Clase2()
print ("al inicio con valores 'self'",ej.resultado)
ej.metodo(6,5)
print ("al finalcon datos modificado por metodo",ej.resultado)
print (input("Fin ej 002_3_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_3
print("Inicio ej 002_3_3 ");
print("############################################################################");
print("##                                                                        ##");
print("##                             y Generadores                              ##");
print("##                                                                        ##");
print("############################################################################");
def Llenar_lista():
	salida=0
	dato_entrada = [1,2,3,4,5,6,7,8,9]
	for elementos in dato_entrada:
		salida+= int(elementos)**2
		print (elementos)
	print (salida)
Llenar_lista()
salida2=0
generada = (elementos for elementos in range(10))
for elementos in generada:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (elementos for elementos in range(10) if elementos%20 == 0)
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (min(elementos,5) for elementos in range(10))
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

print (input("Fin ej 002_3_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_3
print("Inicio ej 002_3_3 ");
print("############################################################################");
print("##                                                                        ##");
print("##                                  Lambda                                ##");
print("##                                                                        ##");
print("############################################################################");

area_triangulo =lambda base,altura:(base*altura)/2
base = float(input("Ingrese la base :"))
altura = float(input("Ingrese la altura :"))
print(area_triangulo(base,altura))
print (input("Fin ej 002_3_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_4
print("Inicio ej 002_3_4 ");

class Counter:
	Count = 0   # This represents the count of objects of this class
	def __init__(self, name):
		self.name = name
		print (name, 'created')
		Counter.Count += 1
	def __del__(self):
		print (self.name, 'deleted')
		Counter.Count -= 1
		if Counter.Count == 0:
			print ('Last Counter object deleted')
		else:
			print (Counter.Count, 'Counter objects remaining')
x = Counter("First")
y = Counter("second")
del x

"""
Without the final del, you get an exception. Shouldn’t the normal cleanup process take care of this?

From the Python docs regarding __del__:

    Warning: Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), other globals referenced by the __del__() method may already have been deleted. For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.

Without the explicit call to del, __del__ is only called at the end of the program, Counter and/or Count may have already been GC-ed by the time __del__ is called (the order in which objects are collected is not deterministic). The exception means that Counter has already been collectd. You can’t do anything particularly fancy with __del__.

There are two possible solutions here.

    1. Use an explicit finalizer method, such as close() for file objects.

        Use weak references.
"""










