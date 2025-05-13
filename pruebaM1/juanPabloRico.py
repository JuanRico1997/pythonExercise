products = [
    {'nameProduct':'Pera','price':4000,'quantify':50},
    {'nameProduct':'Uva','price':6000,'quantify':0},
    {'nameProduct':'Gaseosa','price':2500,'quantify':10}
]
#Check variables, that if they enter the desired value
def verifyInput(mesagge, type=str, extraValidation=None, extraMessageError="Error"):
    while True:
        response = input(mesagge).strip()
        try:
            value = type(response)
            if extraValidation and not extraValidation(value):
                print(f"{extraMessageError}")
                continue
            return value
        except ValueError:
            print(f"Entrada inválida. Ingresa un valor del tipo {type.__name__}.")

#Displays all inventory at any time                
def seeInventory():
    print("----------Inventario----------")
    for product in products:
        print("-"*30)
        print(f"Producto: {product['nameProduct']}")
        print(f"Precio Unitario: {product['price']}")
        print(f"Cantidad Disponible: {product['quantify']}")
        print("-"*30)

#Add a single product, if it is already in inventory, it notifies you       
def addProduct():
    product = input("Ingrese el nombre del producto: ")
    for i in products:
        if i['nameProduct'].lower() == product.lower().strip():
            print("El producto ya está en el inventario.")
            return
    valueProduct = verifyInput(
        mesagge = "Ingrese el valor del producto: ",
        type = float,
        extraValidation =lambda x : x >= 0,
        extraMessageError = "Ingrese un numero valor positivo."
    )
    quantifyProduct = verifyInput(
        mesagge = "Ingrese la cantidad de producto disponible: ",
        type = int,
        extraValidation = lambda x : x>=0,
        extraMessageError = "Ingrese un numero valor positivo."
    )
    newProduct = {'nameProduct':product,'price':valueProduct,'quantify':quantifyProduct}
    products.append(newProduct)
    print("Producto agregado exitosamente al inventario.")

#Search for a product and if it exists, show it, if not, notify that it does not exist  
def findProduct():
    productToFind = input("Busque un producto por su nombre: ")
    for i in products:
        if i['nameProduct'].lower() == productToFind.lower().strip():
            print("Producto Encontrado\n")
            print("-"*30)
            print(f"Producto: {i['nameProduct']}")
            print(f"Precio Unitario: {i['price']}")
            print(f"Cantidad Disponible {i['quantify']}")
            print("-"*30)
            return
    print("El producto NO está en el inventario.")

#Modify the price of the desired product 
def newPrice():
    newPriceProduct = input("Ingrese el nombre del producto que desea actualizar el precio: ")
    for i in products:
        if i['nameProduct'].lower() == newPriceProduct.lower().strip():
            newPrice = float(input("Ingrese el nuevo precio: "))
            while newPrice < 0:
                print("Ingrese un número positivo !!!")
                newPrice = float(input("Ingrese el nuevo precio: "))
            i['price'] = newPrice
            print("Precio actualizado !!")
            return
    print("El producto no está en el inventario.")

#Delete the desired product
def deletProduct():
    nameDeletProduct = input("Ingrese el nombre del producto que desea eliminar: ")
    found = None
    exit = True
    while exit == True:
        for i in products:
            if i['nameProduct'].lower() == nameDeletProduct.lower().strip():
                if i['quantify'] == 0:
                    print(f"El producto tiene {i['quantify']}. Desea eliminarlo?")
                    delet = input("1.SI\n2.NO\n")
                    match delet:
                        case '1':
                            products.remove(i)
                            print("Producto eliminado exitosamente !!")
                            exit = False
                            break
                        case '2':
                            print("No se eliminó el producto")
                            return
                        case _:
                            print("Ingrese una opción valida")
                            break
                            
                else:
                    print(f"El producto todavía tiene {i['quantify']} unidades. Desea eliminarlo?")
                    delet = input("1.SI\n2.NO\n")
                    match delet:
                        case '1':
                            products.remove(i)
                            print("Producto eliminado exitosamente !!")
                            exit = False
                            return
                        case '2':
                            return
                        case _:
                            print("Ingrese una opción valida")
                        
            else:
                print("El producto no está en el inventario.")
                return
    
        

#Displays the products and their total (price*quantity)
def totalInventary():
    
    print("-------TOTAL INVENTARIO-------")
    for i in products:
        print("-"*30)
        total = i['price']*i['quantify']
        print(f"Producto: {i['nameProduct']}")
        print(f"Total acumulado: {total} ")
        print("-"*30)
        totalProducts.append(total)
        
 
def firstMenu():
    NumberProductInto = verifyInput(
            mesagge="Ingrese la cantidad de productos a registrar: ",
            type=int,
            extraValidation=lambda x : x>=0,
            extraMessageError="Ingrese un valor positivo."
        )
    if NumberProductInto >= 5:
        j=0
        while j < NumberProductInto:
            product = input(f"Ingrese el nombre del producto {j+1}: ")
            found = None
            for i in products:
                
                if i['nameProduct'].lower() == product.lower().strip():
                    print("El producto ya está en el inventario.")
                    found = i
                    continue
                    

            if not found:
                valueProduct = verifyInput(
                    mesagge = "Ingrese el valor del producto : ",
                    type = float,
                    extraValidation =lambda x : x >= 0,
                    extraMessageError = "Ingrese un número valor positivo."
                )
                quantifyProduct = verifyInput(
                    mesagge = "Ingrese la cantidad de producto disponible: ",
                    type = int,
                    extraValidation = lambda x : x>=0,
                    extraMessageError = "Ingrese un número valor positivo."
                )
                newProduct = {'nameProduct':product,'price':valueProduct,'quantify':quantifyProduct}
                products.append(newProduct)
                print("Producto agregado exitosamente al inventario.")
                j+=1
    else:
        print("Mínimo se permiten ingresar 5 productos.")
           
def secondMenu():
    while True:
        print("-------Inventario RIWI--------")
        optionMenu = input("""
1.Añadir un nuevo producto.
2.Consultar en el inventario un producto.
3.Actualizar precio de un producto.
4.Eliminar un producto del inventario.
5.Valor total del inventario.
6.Mostrar el inventario.
7.Salir
                    
Elija una opción: """)

        match optionMenu:
            case '1':
                addProduct()
            case '2':
                findProduct()
            case '3':
                newPrice()
            case '4':
                deletProduct()
            case '5':
                totalInventary()
                print("TOTALIDAD EL INVETARIO")
                print(sum(totalProducts))
            case '6':
                seeInventory()
            case '7':
                break
            case _:
                print("Ingrese una opción válida.")            
            
        
while True:
    totalProducts = []
    
    option = input("----BIENVENIDO A NUESTRO SISTEMA----\nMarque una opción\n1.Ingresar productos (Mínimo 5 productos)\n2.Ver menú\n3.Salir\n")
    #Menú principal
    match option:
        case '1':
            firstMenu()
        case '2':    
            secondMenu()
        case '3':
            exit()
        case _:
            print("Ingrese una opción válida.")        
