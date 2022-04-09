"""Ejercicio 8
Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial."""

num = int(input("Ingresar un número"))

def factorial(num):
    <<<<<<< HEAD
    if num == 1:
        return 1                 # num: 5 4 3 2 1
    else:
        return num * factorial(num-1)
print("El factorial es",factorial(num))

