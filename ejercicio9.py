"""Ejercicio 9
Crear una función que calcule el MCD de dos número por el método de Euclides. 
El método de Euclides es el siguiente:
Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD."""

def Metodo_Euclides(num1,num2):

    if num1>num2:
        while num1%num2!=0:
            r=num1%num2
            num1=num2
            num2=r
        return num2
    elif num1<num2:
        while num2%num1!=0:
            r=num2%num1
            num2=num1
            num1=r
        return num1
    else:
        return num2
        
def main():
    print("*MCD*\n Ingresar dos números enteros para calcular su MCD:")
    num1=int(input());num2=int(input())
    print("MCD:",Metodo_Euclides(num1,num2))
main()