"""Ejercicio 7
Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y 
te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer 
login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se 
intente hacer login, solamente tenemos tres oportunidades para intentarlo."""

def login (user,password,n):
    if user == "usuario1" and password == "asdasd": 
        n=0
        return True
    else:
        n+=1
        return False

def main():
    global n
    n=0
    while n<3:
        usuario=str(input("Usuario: "))
        clave=str(input("Contraseña: "))
        if n<3 and login(usuario,clave,n)==True:
            print("Acceso permitido.")
            pass
        else:
            print("El usuario o la clave son incorrectos.")
            n+=1
    if n==3:
        print("Ha completado el  número máximo de intentos.")
main()