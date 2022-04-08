"""Ejercicio 3
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""

max = int(input("Ingresar la temperatura máxima"))
min = int(input("Ingresar la temperatura mínima"))

def temp_media(max, min):
    temp_media = (max+min)/2 
    print("Siendo la temperatura máxima",max,"y la temperatura mínima", min,"su tamperatura media es: ",temp_media)
temp_media(max, min)
