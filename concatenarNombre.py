def formatear_nombre(nombre1,nombre2,apellido):

    nombre1Formateado = nombre1.capitalize()
    nombre2Formateado = nombre2.capitalize()
    apellidoFormateado = apellido.capitalize()


    nombreCompleto = nombre1Formateado + " " + nombre2Formateado + " " + apellidoFormateado
    
    return nombreCompleto


nombre1 = input("Ingrese su primer nombre: ")
nombre2 = input("Ingrese su segundo nombre: ")
apellido = input("Ingrese su apellido: ")


print(formatear_nombre(nombre1,nombre2,apellido))

