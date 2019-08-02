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
print("##                              Bases de Datos                            ##");
print("##                                                                        ##");
print("##                         libreria mysql.connector                       ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Create Database                                ##");
print("##                         Create Table                                   ##");
print("##                         Insert                                         ##");
print("##                         Select                                         ##");
print("##                         Where                                          ##");
print("##                         Order By                                       ##");
print("##                         Delete                                         ##");
print("##                         Drop Table                                     ##");
print("##                         Update                                         ##");
print("##                         Limit                                          ##");
print("##                         Join                                           ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                MySQL has 3 main categories of data types namely        ##");
print("##                                                                        ##");
print("##                               Numeric,                                 ##");
print("##                               Text                                     ##");
print("##                               Date/time.                               ##");
print("##                                                                        ##");
print("##  Numeric Data types                                                    ##");
print("##  Numeric data types are used to store numeric values. It is very       ##");
print("##    important to make sure range of your data is between lower and upper##");
print("##    boundaries of numeric data types.                                   ##");
print("##               TINYINT( )    -128 to 127 normal 0 to 255                ##");
print("##               SMALLINT( )   -32768 to 32767 normal                     ##");
print("##               MEDIUMINT( )  -8388608 to 8388607 normal                 ##");
print("##               INT( )        -2147483648 to 2147483647 normal           ##");
print("##               BIGINT( )     -9223372036854775808 to                    ##");
print("##                           9223372036854775807 normal                   ##");
print("##               FLOAT         A small approximate number with a floating ##");
print("##                   decimal point.                                       ##");
print("##               DOUBLE( , )   A large number with a floating decimal     ##");
print("##                   point.                                               ##");
print("##               DECIMAL( , )  A DOUBLE stored as a string , allowing     ##");
print("##                   for a fixed decimal point. Choice for storing        ##");
print("##                   currency values.                                     ##");
print("##                                                                        ##");
print("##  Text Data Types                                                       ##");
print("##  As data type category name implies these are used to store text values##");
print("##  Always make sure you length of your textual data do not exceed        ##"); 
print("##  maximum lengths.                                                      ##");
print("##               CHAR( )       A fixed section from 0 to 255 characters   ##");
print("##               VARCHAR( )    A variable section from 0 to 255 chrs      ##");
print("##               TINYTEXT      A string with a max. length of 255 chrs.   ##");
print("##               TEXT          A string with a max. length of 65535       ##");
print("##               BLOB          A string with a max. length of 65535       ##");
print("##               MEDIUMTEXT    A string with a max. length of 16777215    ##");
print("##               MEDIUMBLOB    A string with a max. length of 16777215    ##");
print("##               LONGTEXT      A string with a max. length of 4294967295  ##");
print("##               LONGBLOB      A string with a max. length of 4294967295  ##");
print("##                                                                        ##");
print("##  Date / Time                                                           ##");
print("##               DATE          YYYY-MM-DD                                 ##");
print("##               DATETIME      YYYY-MM-DD HH:MM:SS                        ##");
print("##               TIMESTAMP     YYYYMMDDHHMMSS                             ##");
print("##               TIME          HH:MM:SS                                   ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##  Apart from above there are some other data types in MySQL.            ##");
print("##                                                                        ##");
print("##  ENUM     To store text value chosen from a list of predefined text    ##");
print("##           values                                                       ##");
print("##  SET      This is also used for storing text values chosen from a list ##");
print("##           predefined text values. It can have multiple values.         ##");
print("##  BOOL     Synonym for TINYINT(1), used to store Boolean values         ##");
print("##  BINARY   Similar to CHAR, difference is texts are stored in binary    ##");
print("##           format.                                                      ##");
print("##  VARBINARY   Similar to VARCHAR, difference is texts are stored        ##");
print("##              in binary format.                                         ##");
print("##                                                                        ##");
print("############################################################################");
print("https://www.w3schools.com/python/python_mysql_create_db.asp")
print("https://www.w3schools.com/python/python_mysql_create_table.asp");
print("https://www.w3schools.com/python/python_mysql_insert.asp");
print("https://www.w3schools.com/python/python_mysql_select.asp");
print("https://www.w3schools.com/python/python_mysql_where.asp");
print("https://www.w3schools.com/python/python_mysql_orderby.asp");
print("https://www.w3schools.com/python/python_mysql_delete.asp");
print("https://www.w3schools.com/python/python_mysql_drop_table.asp");
print("https://www.w3schools.com/python/python_mysql_update.asp");
print("https://www.w3schools.com/python/python_mysql_limit.asp");
print("https://www.w3schools.com/python/python_mysql_join.asp");
print (r" C:\Users\Your ALUMNO_NOMBRE\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector ");
print("https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html")
print("https://www.guru99.com/how-to-create-a-database.html")
print("http://www.mysqltutorial.org/mysql-datetime/")
print(input("continuo????"))
limpiar();
import mysql.connector
import datetime
#from datetime import date
#from datetime import datetime
def Iniciar_practica():
#	try:
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	accion = input ("Drop la DDBB (S/N)")
	if accion.upper() == "S":
		print ("Borramos la base de datos  UTN_practica_2_2019")
		puntero.execute("DROP DATABASE UTN_practica_2_2019")
	puntero.execute("CREATE DATABASE UTN_practica_2_2019")
	print ("Creamos la base de datos  UTN_practica_2_2019")
	puntero.close
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
	puntero = conectarse.cursor()
	puntero.execute("CREATE TABLE 2017_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
	puntero.execute("CREATE TABLE 2018_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")	
	puntero.execute("CREATE TABLE 2019_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date )")
	columnas_mysql = "INSERT INTO 2019_Marzo (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	nacimiento = datetime.datetime(1973,9,22)
	hoy = datetime.datetime.now()
	ingreso = datetime.datetime(2015,3,1)
	puntero.execute(columnas_mysql, ("Garcia Traba", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia T", "Marisol" , "marisol@gmarisolmail.com","+5491144754637","43","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia T", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia Renzetti", "Facundo" , "facundo.garcia.renzetti@gmail.com","+5491144754637","13","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia Renzetti", "Joaquin" , "joaquin.garcia.renzetti@gmail.com","+5491144754637","9","M",hoy,nacimiento,ingreso))
	conectarse.commit()

	print(puntero.rowcount, "record inserted.")
	puntero.close
def Recargar_practica():
	print ("Recargar_practica Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
	puntero = conectarse.cursor()
	columnas_mysql = "INSERT INTO 2019_Marzo (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	nacimiento = datetime.datetime(1973,9,22)
	hoy = datetime.datetime.now()
	ingreso = datetime.datetime(2015,3,1)
	puntero.execute(columnas_mysql, ("Garcia Traba", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia T", "Marisol" , "marisol@gmarisolmail.com","+5491144754637","43","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia T", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia Renzetti", "Facundo" , "facundo.garcia.renzetti@gmail.com","+5491144754637","13","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Garcia Renzetti", "Joaquin" , "joaquin.garcia.renzetti@gmail.com","+5491144754637","9","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	print(puntero.rowcount, "record inserted.")
	puntero.close

Iniciar_practica()
print(input("continuo????"))
limpiar();
print (input("\n\n  1_1) SELECIONO Y MUESTRO TODO LO QUE TENGA LA TABLA ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
print ('puntero.execute("SELECT * FROM 2019_Marzo")');
puntero.execute("SELECT * FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
print (input("\n\n  1_2) MUESTRO POR FILAS LAS COLUMNAS SELECCIONADAS TODO LO QUE TENGA LA TABLA ?"));
puntero.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO from 2019_Marzo")
print("ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO")
for fila in puntero:
	print(fila)
	print("------------------------------\n")
puntero.close
print (input("\n\n  2) SELECIONO POR COLUMNA ALUMNO_NOMBRE, ALUMNO_MAIL FROM 2019_Marzo ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT ALUMNO_NOMBRE, ALUMNO_MAIL FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  3)SELECCIONO CON FILTROS `WHERE` ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL ='ariel.garcia.traba@gmail.com'"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
print(input("continuo????"))
limpiar();
print (input("\n\n  4 ) * FILTRO CON CARACTERES % wildcard '%LIKE%' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL LIKE '%garcia%'"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  5 ) FILTRO CON CARACTERES %s wildcard  SQL Injection ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL = %s"
adr = ("ariel.garcia.traba@gmail.com", )
puntero.execute(sql, adr)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  6 ) SORT ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM 2019_Marzo ORDER BY ALUMNO_NOMBRE"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  7 ) SORT INVERTIDO ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM 2019_Marzo ORDER BY ALUMNO_NOMBRE DESC"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  8 ) BORRO UN RECORD ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close

sql = "DELETE FROM 2019_Marzo WHERE ALUMNO_MAIL = 'ariel.garcia.traba@gmail.com'"
puntero.execute(sql)
print ("borro - "+ str(sql));
conectarse.commit()
print(puntero.rowcount, "record(s) deleted")

puntero.execute("SELECT * FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  9 ) BORRO UN RECORD - Prevent SQL Injection ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)

sql = "DELETE FROM 2019_Marzo WHERE ALUMNO_NOMBRE = %s"
adr = ("Joaquin", )
print ("borro - "+ str(sql) + str(adr) );
puntero.execute(sql, adr)
conectarse.commit()
print(puntero.rowcount, "record(s) deleted")

puntero.execute("SELECT * FROM 2019_Marzo")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  10 ) ACTUALIZAR UN DATO 'UPDATE' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL LIKE '%garcia%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 

sql = "UPDATE 2019_Marzo SET ALUMNO_MAIL = 'ariel.garcia.traba@ariel.garcia.traba@hotmail.com.com' WHERE ALUMNO_MAIL = 'ariel.garcia.traba@hotmail.com'"
puntero.execute(sql)
conectarse.commit()
print(puntero.rowcount, "record(s) affected")

puntero.execute("SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL LIKE '%garcia%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  11 ) ACTUALIZAR CON %s SQL Injection 'UPDATE' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL LIKE '%garcia%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)

sql = "UPDATE 2019_Marzo SET ALUMNO_MAIL = %s WHERE ALUMNO_MAIL = %s"
val = ("ariel.garcia.traba@hotmail.com", "ariel.garcia.traba@Gmail.com")
puntero.execute(sql, val)
conectarse.commit()
print(puntero.rowcount, "record(s) affected")

puntero.execute("SELECT * FROM 2019_Marzo WHERE ALUMNO_MAIL LIKE '%garcia%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  12 ) LIMITO LA CANTIDAD DE RESULTADOS 'LIMIT' ?"));
print ("You can limit the number of records returned from the query, by using the 'LIMIT' statement:");
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT * FROM 2019_Marzo LIMIT 5")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  13 ) INICIO DESDE OTRA POSICION OFFSET ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT * FROM 2019_Marzo LIMIT 5 OFFSET 2")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()  
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  14 ) BORRO UNA TABLA 'Drop' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")

print ("------------Estado Inicial-------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
print ("------------DROP-----------------------")

puntero = conectarse.cursor()
sql = "DROP TABLE 2019_Marzo"
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)

Iniciar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  15 ) BORRO UNA TABLA 'Drop' SI EXISTE ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

print ("------------Estado Inicial-------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
print ("------------DROP-----------------------")

puntero = conectarse.cursor()
sql = "DROP TABLE IF EXISTS 2020_Marzo"
print( "Tabla a borrar"+str(sql))
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
puntero = conectarse.cursor()
sql = "DROP TABLE IF EXISTS 2019_Marzo"
print( "Tabla a borrar"+str(sql))
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
	
Iniciar_practica()
puntero.close
