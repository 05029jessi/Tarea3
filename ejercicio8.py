"""Ejercicio 8
Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial."""

num = int(input("Ingresar un número"))

def factorial(num):
    print "Valor inicial ->",num 
    if numero > 1:
        num= num*factorial(num-1)
    print "valor final ->",num
    return numero
print("El factorial de",num,"es", num)
