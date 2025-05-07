products = [
    {'nombre': 'Manzana', 'valor': 500, 'existencia': 30},
    {'nombre': 'Banano', 'valor': 300, 'existencia': 20},
    {'nombre': 'Uvas', 'valor': 3000, 'existencia': 25},
    {'nombre': 'Platano', 'valor': 5000, 'existencia': 20}
]

def enterProducts():
    nameProduct = input("Ingrese nombre del producto: ")
    for i in products:
        if i['nombre'].lower() == nameProduct.lower():
            print("El producto ya esta en el inventario.")
            print(f"""Nombre: {i['nombre']} 
Valor: {i['valor']} 
Existencia: {i['existencia']}""")
            return

    valueProduct = float(input("Ingrese el valor del producto: "))
    existenceProducto = int(input("Ingrese la cantidad del producto disponible: "))
    newProducto = {'nombre':nameProduct,'valor':valueProduct,'existencia':existenceProducto}
    products.append(newProducto)
    print(f"El producto {newProducto['nombre']} fue agregado exitosamente")

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
    
def updatePrice():
    print("         --------ACTUALIZAR DATOS--------\n")
    updateProduct = input("Ingrese el producto al que desea actulizar: ")
    count = 0
    for i in products:
        count+=1
        if i['nombre'].lower() == updateProduct.lower():
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
                            newPrice = float(input("Ingrese el nuevo valor del producto : "))
                            i['valor'] = newPrice
                            print("Valor actualizado!")
                            break
                            
                case 3:
                    for i in products:
                        if i['nombre'].lower() == updateProduct.lower():
                            newExistence = int(input("Ingrese la nueva cantidad del producto: "))
                            i['existencia'] = newExistence
                            print("Existencia actualizada!")
                            break
            break                       
        else:
            print("Producto no encontrado !")
            




while True:
    option = int (input("""--------MENÚ PRINCIPAL---------

1.Ingresar producto al sistema
2.Consultar producto
3.Actualizar datos
4.Eliminar producto
5.Valor del inventario
6.Salir\n"""))
    
    match option:
        case 1:
            enterProducts()
        case 2:
            seeProduct()
        case 3:
            updatePrice()
        case 6:
            print(products)     



























      
enterProducts()
seeProduct()
print(products)
    
 