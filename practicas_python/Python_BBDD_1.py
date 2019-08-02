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
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("Inicio ej015_1 -  ");
import mysql.connector
import json
print("#########################################################");
#print ("C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector");
print("https://www.w3schools.com/python/python_mysql_create_db.asp");
print("http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc36272.1550/html/commands/X72692.htm")
print("############################################################################");
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
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                     libreria mysql.connector                           ##");
print("##                                                                        ##");
print("############################################################################");
print("Inicio ej015_1 -  ");
import mysql.connector
print("#########################################################");
print("https://www.w3schools.com/python/python_mysql_create_db.asp")


def crear_base(nombre_base_MySQL):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")#database='AGT',
	puntero = conectarse.cursor()
	puntero.execute("CREATE DATABASE "+str(nombre_base_MySQL))
	print ("Creamos la base de datos "+str(nombre_base_MySQL))
	print ("cerramos coneccion")
	puntero.close
def listar_bases():
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		lista_nombres_bases=str(lista_bases)
		lista_nombres_bases_largo=len(lista_bases)-4
		lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
		print ("*"+lista_nombres_bases+"*")
		lista_de_bases.append(lista_nombres_bases);
	print (lista_de_bases)
	print ("cerramos coneccion")
	puntero.close
	return (lista_de_bases)

def chequear_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	lista_bases_2=json.loads(lista_bases);
	lista_de_bases_2.append(lista_bases_2);
	print(lista_de_bases);
	print(lista_de_bases_2);
	base_nueva=False
	while base_nueva==False:
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
	return (nombre_base_MySQL_input)
	
def listar_tablas(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	print (nombre_base_MySQL_input)
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database=nombre_base_MySQL_input,)
	puntero = conectarse.cursor()
	puntero.execute("SHOW TABLES")
	lista_de_tablas=[]
	print ("cargamos el listado de tabla de la base"+str(nombre_base_MySQL_input))
	for lista_tablas in (puntero):
		print(lista_tablas)
		lista_nombres_tablas=str(lista_tablas)
		print ("*"+str(lista_nombres_tablas)+"*")
		lista_de_tablas.append(lista_nombres_tablas);
	puntero.close
	return (lista_de_tablas)

def borrar_base(nombre_base_MySQL_input):
	limpiar()
	listar_bases()
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("DROP DATABASE "+str(nombre_base_MySQL_input))
	puntero.close

limpiar()
while True:
	print ("\n\n\n");	
	print ("L) listar Base");
	print ("C) Crear Base");
	print ("A) Abrir Base");
	print ("B) Borrar Base");	
	print ("Z) Salir del programa")
	opcion= input("Opcion : ")
	opcion=opcion.upper()
	if opcion =="C":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a CREAR : ")
		crear_base(nombre_base_MySQL)
	elif opcion =="L":
		limpiar()
		listar_bases()
	elif opcion =="A":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a ABRIR : ")
		listar_tablas(nombre_base_MySQL)
	elif opcion =="B":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a BORRAR : ")
		borrar_base(nombre_base_MySQL)
	elif opcion =="Z":
		limpiar()
		break
		
		

"""

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
#print(f"Hola {nombre_base_MySQL} se que tenes {edad} años.")

#func_crear(nuevo_nombre_base_MySQL)
"""
"""
def check_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
#		print ("*"+nombre_base_MySQL_para_chequear+"*", "*"+nombre_base_MySQL_input+"*")
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	c=0
	base_nueva=False
	while base_nueva==False:
		input("while"+str(base_nueva))
		c +=1
		print (c)
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         ==")
				input("=="+str(base_nueva))
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
				else:
					print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         =/=")
					input("=/="+str(base_nueva))
		input("Fin"+str(base_nueva))
	print (lista_de_bases)
	print (nombre_base_MySQL_input)
	return (nombre_base_MySQL_input)
nombre_base_MySQL= "mysql"#input("Ingrese el nombre de la base de datos MySQL : ")
print(check_base_existe(nombre_base_MySQL))
"""
