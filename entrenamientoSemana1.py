

total = 0

print("Desea registrar un producto? ")
regProducto = int (input("1. Si ----------- 2. No\n"))


while regProducto == 1 :

    nombreProducto = input("Ingrese el nombre del producto: ")
    while not nombreProducto.isalpha():
        print("SOLO SE PERMITE INGRESAR NOMBRE DE PRODUCTOS")
        nombreProducto = input("Ingrese el nombre del producto: ")


    precioUnitario = float(input("Ingrese el precio unitario del producto: "))
    cantidad = int (input("Ingrese la cantidad que desea llevar: "))

    if precioUnitario < 0 or cantidad < 0:
        print("Ingrese un valor positivo")
    else:
        total = precioUnitario * cantidad
        
        

    print("Tiene descuento?")
    des = int (input("1. Si ----------- 2. No\n"))


    if des == 1:
        descuento = float (input("Ingrese el valor del descuento: "))
        descuento = descuento / 100
        totalDesc = total - (total * descuento) 
        print("Nombre del producto: ", nombreProducto)
        print("Cantidad a llevar: ", cantidad)
        print("Precio total: ", total)
        print ("El descuento es: ",(total * descuento))
        print ("El total incluido el descuento es: \n", totalDesc)

    else:
        print("El producto no tiene descuento")
        print("Nombre del producto: ", nombreProducto)
        print("Cantidad a llevar: ", cantidad)
        print("Precio total: \n", total)

    print("Desea registrar un producto? ")
    regProducto = int (input("1. Si ----------- 2. No\n"))
    


