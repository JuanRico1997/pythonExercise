genres = ['Ficcion','Non-ficcion','Ciencia','Biografia','Niños']

libros = {
    '001' : {'Nombre': "Harry Potter",'Autor' : 'JJ K','Año': '2010','Disponibles':10,'Genero Literario':'Ficcion'},
    '002' : {'Nombre': "El señor de los anillos",'Autor' : 'Tolking K','Año': '1010','Disponibles':10,'Genero Literario':'Ficcion'},
    '003' : {'Nombre': "Crimen y castigo",'Autor' : 'Fiódor Dostoyevski.','Año': '1866','Disponibles':0,'Genero Literario':'Psicologia'},
    '004' : {'Nombre': "Sobre la generación y la corrupcion",'Autor' : 'Aristoteles','Año': '384 a.C','Disponibles':7,'Genero Literario':'Biografia'},
    '005' : {'Nombre': "Crimen y castigo",'Autor' : 'Fiódor Dostoyevski.','Año': '1866','Disponibles':0,'Genero Literario':'Psicologia'}
}
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
            print(f"{extraErrorMsg}")

def addBook():
    count = 0
    idNewBook = input("Ingrese el ID del nuevo libro: ")
    if idNewBook in libros:
        print(f"El libro {libros[idNewBook]['Nombre']} ya está en la bibiloteca")
    else:
        nameBook = input("Ingrese el nombre del libro: ")
        nameAutor = input("Ingrese el nombre del autor: ")
        yearPublic = verifyInput(   msg = "Ingrese el año de publicación: ",
                                    type = int,
                                    extraValidation = lambda x : -5000 < x <= 2025,
                                    extraErrorMsg = "Ingrese un año entre -5000 y 2025.")
        quantityBooks = verifyInput(msg = "Ingrese la cantidad de libros en stock: ",
                                    type = int,
                                    extraValidation = lambda x : x>=0,
                                    extraErrorMsg = "Ingrese un numero positivo.")
        for i in genres:
            print(f"{count+1}.{i}")
            count+=1
        genero = input("Ingrese el género del libro: ")
        for i in enumerate(genres):
            if int(genero)-1 == i[0]:
                newgenre = i[1]
        match genero:
            case '1':
                genre = newgenre
            case '2':             
                genre = newgenre
            case '3':             
                genre = newgenre
            case '4':             
                genre = newgenre
            case '5':             
                genre = newgenre
                
            
        libros[idNewBook] = {'Nombre':nameBook,'Autor' : nameAutor,'Año':yearPublic,'Disponibles':quantityBooks,'Genero Literario':genre}
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
    criterio = input("""Desea eliminar libro?
1.Por iD.
2.Por nombre.\n""")
    print(libros.keys())
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
            print("")
            for libro in enumerate(libros.values()):
                print(libro)
                if removeName.lower() == libro[1]['Nombre'].lower():
                    index = libro[0]
                    count = 0
                    for key in libros:
                        if (count == index):
                            libros.pop(key)
                            break
                        count += 1
                    break
            print(libros.keys())
            
def forGenre():
    genre = input("""Géneros:
1.Ficción
2.Non-Ficción
3.Ciencia
4.Biografia
5.Para niños\n""")
    
    actualGenre = genres[int(genre) - 1]
    
    for i in libros.values():
        if i['Genero Literario'] == actualGenre:
            print(f"Nombre: {i['Nombre']}")
            print(f"Autor: {i['Autor']}")
            print(f"Disponibles: {i['Disponibles']}")
            print(f"Género: {i['Genero Literario']}")
                            
            

        
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
        case '6':
            forGenre()
        case '7':
            print("-"*30)
            print("---------BIBLIOTECA ACTUALIZADA---------")
            print("-"*30)
            for i in libros.values():
                print("-"*30)
                print(f"Libro: {i['Nombre']}")
                print(f"Autor: {i['Autor']}")
                print(f"Año de publicacion: {i['Año']}")
                print(f"Copias disponibles: {i['Disponibles']}")
                print(f"Género: {i['Genero Literario']}")
                print("-"*30)
        case _:
            print("Ingrese una opcion valida")
