def suma(a,b):
    return a + b
def resta(a,b):
     return a - b
def multiplicacion(a,b):
     return a * b
def division(a,b):
     return a / b 
def modulo(a,b):
     return a % b 
def pedirDatos():
    num1 = float(input("Ingrese numero 1: "))
    num2 = float(input("Ingrese numero 2: "))
    return num1 , num2




print("Desea ingresar al menu ?:")
menu = int(input("""
1.SI
2.NO\n"""))
if menu == 1:
    menu = True
else:
    menu = False

while menu:
        (print("""-----CALCULADORA-----
1.Suma
2.Resta
3.Multiplicacion
4.Division exacta
5.Modulo
6.Salir\n""")) 
        operation = int (input("\n Seleccion una opcion: "))

        if operation>0 and operation<=6:
 
            

            match operation:
                case 1:
                    datos = pedirDatos()
                    print(suma(datos[0],datos[1]))
                case 2:
                    datos = pedirDatos()
                    print(resta(datos[0],datos[1]))
                case 3:
                    datos = pedirDatos()
                    print(multiplicacion(datos[0],datos[1]))
                case 4:
                    datos = pedirDatos()
                    print(division(datos[0],datos[1]))
                case 5:
                    datos = pedirDatos()
                    print(modulo(datos[0],datos[1]))
                case 6:
                    break
        else:
             print("Ingrese una opcion valida.")

             
        print("Desea volver al menu ?:")
        menu = int(input("""
    1.SI
    2.NO\n"""))
        if menu == 1:
            menu = True
        else:
            menu = False
        
        

      

        


