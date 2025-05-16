products = [{'Nombre':'Pizza Hawaiana','Ingredientes':['Masa','Queso','Jamón','Piña'],'Precio':{'Pequeña':15000,'Mediana':30000,'Grande':60000}},
            {'Nombre':'Pizza Paisa','Ingredientes':['Masa','Queso','Jamón','Tocineta'],'Precio':{'Pequeña':15000,'Mediana':30000,'Grande':60000}},
            {'Nombre':'a','Ingredientes':['Masa','Queso','Jamón','Tocineta'],'Precio':{'Pequeña':15000,'Mediana':30000,'Grande':60000}}]
orders = []
inventary = [{'Nombre':'Masa','Cantidad':50},{'Nombre':'Queso','Cantidad':50},{'Nombre':'Piña','Cantidad':50},{'Nombre':'Jamón','Cantidad':50},{'Nombre':'Tocineta','Cantidad':50},{'Nombre':'Salami','Cantidad':50},{'Nombre':'Peperoni','Cantidad':50}]

#----------------Menú Inventario------------------
def addProductInventary():
    newIngredient = input("Ingrese el nombre del ingrediente: ")
    for i in inventary:
        if i['Nombre'].lower() == newIngredient.lower():
            print("El ingrediente ya está en el inventario.")
            print(f"Nombre: {i['Nombre']}")
            print(f"Cantidad: {i['Cantidad']}")
            return
    quantify = input("Ingrese la cantidad disponible en el inventario: ")
    ingredientNew = {'Nombre':newIngredient,'Cantidad':quantify}
    inventary.append(ingredientNew)

def modifyProductInventary():
    nameProductModify = input("Ingrese el nombre del producto: ")
    found = None
    for i in inventary:
        if i['Nombre'].lower() == nameProductModify.lower():
            found = i
            break
    if found:
        while True:
            option = input("""¿Qué desea modificar?
1.Nombre.
2.Cantidad en inventario.
3.Salir\n""")
            match option:
                case '1':
                    for i in inventary:
                        if nameProductModify.lower() == i['Nombre'].lower():
                            newName = input("Ingrese el nuevo nombre: ")
                            i['Nombre'] = newName
                            print("Nombre modificado exitosamente!")
                            break
                    break    
                case '2':
                    for i in inventary:
                        if nameProductModify.lower() == i['Nombre'].lower():
                            newQuantify = int(input("Ingrese la nueva cantidad:"))
                            found['Cantidad'] = newQuantify
                            print("Cantidad modificada exitosamente!")
                            break
                    break
                case '3':
                    break
                case _:
                    print("Ingrese una opción valida") 
    else:
        print("Producto no encontrado.")    

def removeProductInventary():
    found = None
    nameRemoveProduct = input("Ingrese el nombre del producto que desea eliminar: ")
    for i in inventary:
        if nameRemoveProduct.lower() == i['Nombre'].lower():
            found = i
            print("Está seguro que desea eliminar el producto?\n1.Si\n2.No")
            optionRemove = input("")
            while True:
                match optionRemove:
                    case '1':
                        inventary.remove(i)
                        print("Producto eliminado exitosamente!")
                        break
                    case '2':
                        print("No se eliminó el producto!")
                        break
                    case _:
                        print("Ingrese una opción valida.")
                        print("Está seguro que desea eliminar el producto?\n1.Si\n2.No")
                        optionRemove = input("")
                        continue
                        
    if not found:
        print("El producto no se encuentra en el inventario.")
            
def menuInventary():
    while True:
        option = input("""----------MENÚ INVENTARIO------------
Ingrese una opción:\n
1.Ingresar producto al inventario.
2.Modificar producto.
3.Eliminar producto del inventario.
4.Mostrar inventario.
5.Salir\n""")
        match option:
            case '1':
                addProductInventary()
            case '2':
                modifyProductInventary()
            case '3':
                removeProductInventary()
            case '4':
                seeInventary()
            case '5':
                break
            case _:
                print("Ingrese una opción valida.")     
#----------------Menú Inventario------------------



#----------------Menú Carta-----------------------
def seeProducts():
    print("-----------------------------MENÚ---------------------------")
    for i in products:
        print("--"*30)
        print(f"Nombre: {i['Nombre']}")
        value =i['Ingredientes']
        print("Ingredientes: " + ' '.join(value))
        print("Pequeña: 15000 - Mediana: 30000 - Grande: 60000")
        print("--"*30)

def seeInventary():
    print("-----------INVENTARIO---------")
    for i in inventary:
        print("-"*30)
        print(f"Nombre: {i['Nombre']}")
        print(f"Cantidad: {i['Cantidad']}")     

def addProduct():
    ingredients = []
    ingredientProducto = []
    nameProduct = input("Ingrese el nuevo producto: ")
    for i in products:
        if nameProduct.lower() == i['Nombre'].lower():
            print("El producto ya está en el menú")
            print(f"Nombre: {i['Nombre']}")
            print(f"Ingredientes: {i['Ingredientes']}")
            print(f"Precio: {i['Precio']}")
            return
    print("Elija los ingredientes que lleva el nuevo producto:")
    while True:    
        counter = 0
        if len(ingredients)<1:
            for i in inventary:
                print(f"{counter+1}.{i['Nombre']}")
                ingredients.append(i['Nombre']) 
                counter+=1
            salir = len(ingredients)+1
            print(f"{salir}.Salir")    
        
        ingredient = int(input(""))
        if ingredient >= salir:
            break
        ingredientProducto.append(ingredients[ingredient-1])
        continue
    print(ingredientProducto)
    products.append({'Nombre':nameProduct,'Ingredientes':ingredientProducto,'Precio':"Pequeña: 15000 , Mediana:30000 , Grande:60000"})
    print("Producto agregado al menú exitosamente!")

def modifyProduct():
    productModify = input("Ingrese el nombre del producto a modificar: ")
    for i in products:
        if productModify.lower() == i['Nombre'].lower():
            option = input("¿Qué desea modificar?\n1.Nombre.\n2.Ingredientes.\n3.Precio.\n")
            match option:
                case '1':
                    for i in products:
                        if productModify.lower() == i['Nombre'].lower():
                            newName = input("Ingrese el nuevo nombre: ")
                            i['Nombre'] = newName
                            print("Nombre cambiado exitosamente")
                case '2':
                    optionEdit =input("1.Agregar ingrediente.\n2.Eliminar Ingrediente.\n")
                    match optionEdit:
                        case '1':
                            for i in products:
                                if productModify.lower() == i['Nombre'].lower():
                                    values = i['Ingredientes']
                                    print(f"Ingredientes actuales: "+' '.join(values))
                                    print(f"Listado de ingredientes en la pizzeria: ")
                                    listIngredient = []
                                    for i in inventary:
                                        listIngredient.append(i['Nombre'])
                                    salir = len(listIngredient)+1
                                    print(" ".join(f"{i+1}.{ing}" for i, ing in enumerate(listIngredient))+f" {salir}.Salir")
                                    print("Elija los ingredientes que desea agregar al producto:")
                                    while True:
                                        addIngredient = int(input(""))
                                        if addIngredient >= salir:
                                            print("Productos agregados exitosamente!")
                                            break
                                        found = None
                                        for i in values:
                                            if i == listIngredient[addIngredient-1]:
                                                print("El ingrediente ya está en el producto!")
                                                continue                                       
                                              
                                            values.append(listIngredient[addIngredient-1])
                                                
                                        
                                        
                                                
                                     
                                     
                            
                        
        
def menu():
    while True:
        print("---------MENÚ PRODUCTOS--------")
        option = input("""
1.Agregar producto al menú.
2.Modificar producto.
6.Ver menú.
7.Salir.\n""")
        match option:
            case '1':
                addProduct()
            case '2':
                modifyProduct()
            case '6':
                seeProducts()
            case '7':
                break
            case _:
                print("Ingrese una opción valida.")


            
#----------------Menú Carta-----------------------       

while True:
    
    
    print("-------PIZZERIA JUAN--------")
    optionMenu = input("""
1.Invetario
2.Menú
3.Pedidos
4.Salir\n

Elija una opción: """)
    
    match optionMenu:
        case '1':
            menuInventary()
        case '2':
            menu()
        case '4':
            break
        case _:
            print("Ingrese una opción valida.")
              