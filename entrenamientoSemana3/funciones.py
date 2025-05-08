usuario1 = ("Juan","123456789") #Contraseñas para ingresar al menú
products = [
    {'nombre': 'Manzana', 'valor': 500, 'existencia': 30},
    {'nombre': 'Banano', 'valor': 300, 'existencia': 20},
    {'nombre': 'Uvas', 'valor': 3000, 'existencia': 25},
    {'nombre': 'Platano', 'valor': 5000, 'existencia': 20}
]
#Funcion para verificar un dato y doble validacion por si se necesita otra que cumpla otro requisito
def verifyInput(msg, type=str, extraValidation=None, extraErrorMsg="Error"):
    while True:
        response = input(msg).strip()
        try:
            value = type(response)
            if extraValidation and not extraValidation(value):
                print(f"{extraErrorMsg}")
                continue
            return value
        except ValueError:
            print(f"Entrada inválida. Ingresa un valor del tipo {type.__name__}.")

#Funcion para mostrar todo el valor del inventario
def totalInvetory():
    
    sumeValues = []
    for i in products:
        suma = 0 
        totalValue = i['valor']*i['existencia']
        i['valorTotal'] = totalValue
        suma+=totalValue
        sumeValues.append(suma)
    return sumeValues 

#Funcion para ingresar un producto nuevo        
def enterProducts():
    nameProduct = input("Ingrese nombre del producto: ")
    for i in products:
        if i['nombre'].lower() == nameProduct.lower():
            print("El producto ya esta en el inventario.")
            print(f"""Nombre: {i['nombre']} 
Valor: {i['valor']} 
Existencia: {i['existencia']}""")
            return

    valueProduct = verifyInput(
        msg = "Ingrese el valor del producto: ", 
        type=float,
        extraValidation=lambda  x : x > -1,
        extraErrorMsg="El número es negativo. Ingresa un valor positivo."
    )

    existenceProducto = verifyInput(
        msg = "Ingrese la cantidad del producto: ",
        type = int,
        extraValidation = lambda value : value > -1,
        extraErrorMsg="El número es negativo. Ingresa un valor positivo."
    )
    newProducto = {'nombre':nameProduct,'valor':valueProduct,'existencia':existenceProducto}
    products.append(newProducto)
    print(f"El producto {newProducto['nombre']} fue agregado exitosamente")

#Funcion para buscar un producto en el inventario
def seeProduct():
    nameSearch = input("Ingrese el nombre del producto a buscar: ")
    found = None
    for i in products:
        if i['nombre'].lower() == nameSearch.lower():
            found = i
            break
    if found:
        print(f"""
                    Nombre del producto: {found['nombre']}
                    Precio del producto: {found['valor']}
                    Cantidad producto:   {found['existencia']}""")
    else:
        print("Producto no encontrado")

#Funcion para modificar nombre, precio o cantidad en inventario    
def updatePrice():
    print("         --------ACTUALIZAR DATOS--------\n")
    updateProduct = input("Ingrese el producto al que desea actualizar: ")
    found = None
    for i in products:   
        if i['nombre'].lower() == updateProduct.lower():
            found = i
            break
    if found:
        update = int(input("""
    
1.Actualizar nombre
2.Actualizar precio
3.Actualizar existencia\n"""))
            
        match update:
                
            case 1:
                for i in products:
                    if i['nombre'].lower() == updateProduct.lower():
                        newName = input("Ingrese el nuevo nombre del producto: ")
                        i['nombre'] = newName
                        print("Nombre actualizado!")
                        break
                        
            case 2:
                for i in products:
                    if i['nombre'].lower() == updateProduct.lower():
                        newPrice = verifyInput(
                            msg = "Ingrese el nuevo precio del producto: ",
                            type = float,
                            extraValidation = lambda value : value > -1,
                            extraErrorMsg="El número es negativo. Ingresa un valor positivo."
                        )
                        i['valor'] = newPrice
                        print("Valor actualizado!")
                        break
                        
            case 3:
                for i in products:
                    if i['nombre'].lower() == updateProduct.lower():
                        newExistence = verifyInput(
                            msg = "Ingrese la nueva cantidad de inventario",
                            type = int ,
                            extraValidation = lambda value : value >-1,
                            extraErrorMsg = "El número es negativo. Ingresa un valor positivo."
                        )
                        i['existencia'] = newExistence
                        print("Existencia actualizada!")
                        break
            
    else:
        print("Producto no encontrado !")

#Funcion para eliminar un producto de la lista
def removeProduct():
    remove = input("Ingrese el nombre del producto a eliminar: ")
    found = None
    for i in products:
        if i['nombre'].lower() == remove.lower():
            found = i
            break
    if found:
        products.remove(i)
        print("El producto se ha eliminado de manera correcta.")
    else:
        print("Producto no encontrado en inventario.")

#Funcion para mostrar el inventario    
def inventory():
    for i in products:
        print(f"Producto: {i['nombre']}")
        print(f"Precio por unidad: {i['valor']} $")                 
        print(f"{i['existencia']} unidad(es) en inventario.")
        print(f"Precio total en inventario: {i['valorTotal']} $")
        print("-"*40)


def main():
    quantity1 = 3 # Contador para bloquear usuario
    nameUser = input("Ingrese su usuario: ")
    passWord = input("Ingrese su contraseña: ")
    
    while True:
        if nameUser == usuario1[0] and passWord == usuario1[1]:
            
        
            while True:
                totalInvetory()
                
                option =  input("""--------MENÚ PRINCIPAL---------

1.Ingresar producto al sistema
2.Consultar producto
3.Actualizar datos
4.Eliminar producto
5.Valor del inventario
6.Mostrar inventario
7.Salir\n""")
                
                match option:
                    case '1':
                        enterProducts()
                    case '2':
                        seeProduct()
                    case '3':
                        updatePrice()
                    case '4':
                        removeProduct()
                    case '5':
                        sumeTotallambda = lambda x : sum(x)
                        print(f"La suma de todo el inventario es {sumeTotallambda(totalInvetory())}")
                        print(totalInvetory())
                    case '6':
                        inventory()
                    case '7':
                        exit()
                    case _:
                        print("Por favor, asegúrese de ingresar un valor numérico válido.")
                        continue
        else:
            
            print(f"Usuario o contraseña incorrecta.Le quedan {quantity1} intentos")
            nameUser = input("Ingrese su usuario: ")
            passWord = input("Ingrese su contraseña: ")
            quantity1-=1
            if quantity1<=0:
                print("Usuario bloqueado")
                exit()
        
                    
            
main()        
            

            
            
        
            
         



























      
enterProducts()
seeProduct()
print(products)
    
 