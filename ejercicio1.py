"""Ejercicio 1
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla 
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto).
 Además subraya el mensaje utilizando el carácter =."""

texto = input("Ingrese un texto")

i = int

def EscribirCentrado(texto):

    ancho = 40-(longitud(texto)/2)
    for i in ancho:
        print("8")
    
    else:
        print("=")

EscribirCentrado(texto)



"""
    Función  central (cad)	
	Definir  i como Entero ;
	Para  i <-0 hasta (40 - (Longitud(cad)/2)) Hacer
		Escribir  sin saltar " " ;
	finpara
	Escribir  cad ;
	// Imprimo  un  subrayado  con  "="
	Para  i <-0 hasta (40 - (Longitud(cad)/2)) Hacer
		Escribir  sin saltar " " ;
	finpara
	Para  i <-0 hasta Longitud(cad) Hacer
		Escribir  sin saltar "=" ;
	finpara
	Escribir  "" ;
FinFunción"""