"""Ejercicio 10
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
convertir a horas,minutos y segundos o salir del programa."""

import math

print("\nIngrese la cantidad de minutos")     
in_min=int(input())                        
horas = in_min/60

deci, entero = math.modf(horas)                      
minutos = deci*60
deci_min, entero_min = math.modf(minutos)

print(int(in_min),"minutos son",int(entero),"horas y", int(entero_min), "minutos.")    