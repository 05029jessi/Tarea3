"""Ejercicio 6
Diseñar una función que calcule el área y el perímetro de una circunferencia.
 Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
 muestre su área y perímetro."""

import math   #importar función matemática
pi = math.pi

def area(radio):
    area1 = pi*radio**2
    print("Él área de un círculo es", round(area1,2))
area(5)

def perimetro(radio):
    perimetro1 = 2*pi*radio
    print("Él área de un perímetro es", round(perimetro1,2))
perimetro(5)
