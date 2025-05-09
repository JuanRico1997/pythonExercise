genres = ['fiction']

libros = {
    '001' : {'Nombre': "Harry Potter",'Autor' : 'JJ K','Año': '2010','Disponibles':10,'Genero Literario':'Ficcion'},
    '002' : {'Nombre': "El señor de los anillos",'Autor' : 'Tolking K','Año': '1010','Disponibles':10,'Genero Literario':'Ficcion'},
    '003' : {'Nombre': "Crimen y castigo",'Autor' : 'Fiódor Dostoyevski.','Año': '1866','Disponibles':0,'Genero Literario':'Psicologia'}
}
def addBook():
    idNewBook = input("Ingrese el ID del nuevo libro: ")
    if idNewBook in libros:
        print("El libro ya esta en la bibiloteca")
        print(libros[idNewBook])
    else:
        nameBook = input("Ingrese el nombre del libro: ")
        nameAutor = input("Ingrese el nombre del autor: ")
        yearPublic = input("Ingrese el año de publicacion del libro: ")
        quantityBooks = input("Ingrese la cantidad de libros en stock: ")
        genre = input("Ingrese el género del libro: ")
        libros[idNewBook] = {'Nombre':nameBook,'Autor' : nameAutor,'Año':yearPublic,'disponibles':quantityBooks,'generoLiterario':genre}
        print("Libro agregado exitosamente!!!")

def searchBook():
    criterio = input("Desea buscar el libro por iD INGRESE ID / Desea buscar el libro por titulo INGRESE TITULO: ")
    if criterio.lower() == "id":
        idBook = input("Ingrese el Id del libro: ")
        if idBook in libros:
            print(f"Libro encontrado : {libros[idBook]}")
        else:
            print("El libro no esta en la biblioteca.")
    if criterio.lower() == "titulo":
        nameBook = input("Ingrese el titulo del libro: ")
        found = False
        for i in libros.values():
            if i['Nombre'].lower() == nameBook:
                print(i)
                found = True
        if not found:
            print("Libro no encontrado")

def registerLoan():
    bookLoan = input("Titulo del libro desea prestar: ").lower()
    for i in libros.values():
        if bookLoan in i['Nombre'].lower():
            if i['Disponibles'] < 1:
                print("El libro no esta disponible.")
            else:
                print("El libro esta disponible")
                i['Disponibles']-=1

def returnBook():
    bookReturn = input("Titulo del libro a devolver: ")
    found = False
    for i in libros.values():
        if bookReturn in i['Nombre'].lower():
            print(f"Libro {bookReturn}  devuelto exitosamente.")
            i['Disponibles']+=1
            found = True
    if not found:
        print(f"El libro {bookReturn} no esta en la biblioteca.")
        
def removeBook():
    print(libros.keys())
    criterio = input("""Desea eliminar libro?
1.Por iD.
2.Por nombre.\n""")
    match criterio:
        case '1':
            found = False
            removeId = input("Ingrese el iD del libro que desea eliminar: ")
            if removeId in libros.keys():
                found = True
                if found:
                    libros.pop(removeId)
                    print(f"EL libro con el ID {removeId} fue eliminado exitosamente!")
            if not found:
                print(f"El libro con  ID {removeId} no se encuentra en la biblioteca!")
        case '2':
            found = False
            removeName = input("Ingrese el nombre del libro que desea eliminar: ")
            for i in libros.values():
                if removeName.lower() in i['Nombre'].lower():
                    found = True
                    if found:
                        print("ENTRE")         
                    
                
                
                
            
                    
            
        
while True:

    print("""------BIBLIOTECA RIWI-------
1.Añadir Libros a la biblioteca
2.Buscar libro
3.Registar préstamo de libro
4.Devolver Libro
5.Eliminar libros del catálogo
6.Listar libros por género
7.Resumen Inventario""")

    option = input("Ingrese una opcion:")

    match option:
        case '1':
            addBook()
        case '2':
            searchBook()
        case '3':
            registerLoan()
        case '4':
            returnBook()
        case '5':
            removeBook()
        case '7':
            for i in libros.values():
                print("-"*30)
                print("---------BIBLIOTECA ACTUALIZADA---------")
                print("-"*30)
                print(f"Libro: {i['Nombre']}")
                print(f"Autor: {i['Autor']}")
                print(f"Año de publicacion: {i['Año']}")
                print(f"Copias disponibles: {i['Disponibles']}")
                print(f"Género: {i['Genero Literario']}")
                print("-"*30)
        case _:
            print("Ingrese una opcion valida")
