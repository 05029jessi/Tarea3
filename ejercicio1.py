"""Ejercicio 1
Crea un función EscribirCentrado, que reciba como parámetro un text y lo escriba centrado en pantalla 
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 separacions antes del text).
 Además subraya el mensaje utilizando el carácter =."""

def EscribirCentrado(column,text):
    separacion=int(column/2)-(int(len(text)/2))

    for i in range(0,separacion):
        print(end =" ")
    print(text)

    for j in range(0,separacion):
        print(end =" ")

    for k in range(0,len(text)):
        print(end ="=")

EscribirCentrado(80,"Curso Python Marzo 2022")