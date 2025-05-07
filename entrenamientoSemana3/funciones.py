products = [
    {'nombre': 'Manzana', 'valor': 500, 'existencia': 30},
    {'nombre': 'Banano', 'valor': 300, 'existencia': 20}
]

def enterProducts():
    nameProduct = input("Ingrese nombre del producto: ")
    encontrado = products[0].values()
    print(encontrado)
    if nameProduct in encontrado:
        print("Este producto ya existe.")
        return
    valueProduct = float(input("Ingrese el valor del producto: "))
    existenceProducto = int(input("Ingrese la cantidad del producto disponible: "))
    products.append({'nombre':nameProduct,'valor':valueProduct,'existencia':existenceProducto})
    print("Producto agregao exitosamente")

def seeProduct():
    nameSearch = input("Ingrese el nombre del producto a buscar: ")
    encontrado = None
    for producto in products:
        if producto['nombre'].lower() == nameSearch.lower():
            encontrado = producto
            break
    if encontrado:
        print(f"""Nombre del producto: {encontrado['nombre']}
                  Precio del producto: {encontrado['valor']}
                  Cantidad producto:   {encontrado['existencia']}""")
    else:
        print("Producto no encontrado")
    
   
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



























      
enterProducts()
seeProduct()
print(products)
    
 