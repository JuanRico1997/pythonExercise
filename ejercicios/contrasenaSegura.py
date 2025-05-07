def secure_password (password):

    tiene_ocho_caracteres = len(password)>=8
    tiene_mayuscula = any(c.isupper for c in password)
    tiene_numeros = any(c.isdigit for c in password)
    
    return tiene_ocho_caracteres and tiene_mayuscula and tiene_numeros



password = input("Ingrese su contraseña: ")


print (secure_password(password))