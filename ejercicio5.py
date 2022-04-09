"""Ejercicio 5
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo 
y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando 
la función anterior.""" 

def calcularMaxMin(lista_num):
        maximo=max(lista_num)
        minimo=min(lista_num)
        print("El valor máximo es:",maximo)
        print("El  valor mínimo es:",minimo)

def main():
    n1=int(input("Ingresar una cierta cantidad de valores: "))
    lista=[]
    print("Ingresar los valores: ")
    for i in range(0,n1):
        n2=int(input())
        lista.append(n2)
    calcularMaxMin(lista)
main()