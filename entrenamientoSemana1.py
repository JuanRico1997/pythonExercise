total = 0


print("Desea registrar un producto? ")

regProducto = input("1. Si ----------- 2. No\n")
while not regProducto.isnumeric():
    print("Ingrese una opcion valida")
    regProducto = input("1. Si ----------- 2. No\n")

# DATOS DE ENTRADA DEL USUARIO
    
while int(regProducto) == 1 :

    nombreProducto = input("Ingrese el nombre del producto: ")
    while not nombreProducto.isalpha():
        print("SOLO SE PERMITE INGRESAR NOMBRE DE PRODUCTOS")
        nombreProducto = input("Ingrese el nombre del producto: ")


    precioUnitario = input("Ingrese el precio unitario del producto: ")
    while not precioUnitario.isnumeric():
        print("SOLO SE PERMITE INGRESAR NUMEROS")
        precioUnitario = input("Ingrese el numero: ")
    

    cantidad = input("Ingrese la cantidad que desea llevar: ")
    while not cantidad.isnumeric():
        print("SOLO SE PERMITE INGRESAR NUMEROS")
        cantidad = input("Ingrese el numero: ")
    
    # PROCESAMIENTO DE DATOS

    if int(precioUnitario) < 0 or int(cantidad) < 0:
        print("Ingrese un valor positivo")
    else:
        total = int(precioUnitario) *int(cantidad)
        
        

    print("Tiene descuento?")
    des = int (input("1. Si ----------- 2. No\n"))

    # SALIDA DE DATOS

    if des == 1:
        descuento = float (input("Ingrese el valor del descuento: "))
        descuento = descuento / 100
        totalDesc = total - (total * descuento) 
        print("Nombre del producto: ", nombreProducto.capitalize())
        print("Cantidad a llevar: ", cantidad)
        print("Precio total: ", total)
        print ("El descuento es: ",(total * descuento))
        print ("El total incluido el descuento es: \n", totalDesc)

    else:
        print("El producto no tiene descuento")
        print("Nombre del producto: ", nombreProducto.capitalize())
        print("Cantidad a llevar: ", cantidad)
        print("Precio total: \n", total)

    print("Desea registrar un producto? ")
    regProducto = int (input("1. Si ----------- 2. No\n"))
    


