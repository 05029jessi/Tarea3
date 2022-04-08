"""Ejercicio 2
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

num1 = int(input("Ingresar el primer número"))
num2 = int(input("Ingresar el segundo número"))


def EsMultiplo(num1, num2):
    if num1 % num2 == 0:
        mult = True
        print(num1, "es multiplo de", num2)
    else:
        mult = False
        print(num1, "no es multiplo de", num2)

EsMultiplo(num1, num2)