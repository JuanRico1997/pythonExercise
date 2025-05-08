genres = []

libros = {
    '001' : {'Nombre': "Harry Potter",'Autor' : 'JJ K','Año': '2010','disponibles':'10','generoLiterario':'Ficcion'},
    '002' : {'Nombre': "El señor de los anillos",'Autor' : 'Tolking K','Año': '1010','disponibles':'10','generoLiterario':'Ficcion'}
}
def addBook():
    idNewBook = input("Ingrese el ID del nuevo libro: ")
    if idNewBook in libros:
        print("El libro ya esta en la bibiloteca")
    else:
        nameBook = input("Ingrese el nombre del libro: ")
        nameAutor = input("Ingrese el nombre del autor: ")
        yearPublic = input("Ingrese el año de publicacion del libro: ")
        quantityBooks = input("Ingrese la cantidad de libros en stock: ")
        genre = input("Ingrese el género del libro: ")
    

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
        case _:
            print("Ingrese una opcion valida")
    