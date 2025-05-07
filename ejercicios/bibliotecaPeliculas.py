bibliotecaPeliculas = {
    '001' : {'titulo':'Harry Potter y La Piedra Filosofal','productor':'David Heyman','año':'2001'},
    '002' : {'titulo':'El Hobbit','productor':'Peter Jackson','año':'2012'},
    '003' : {'titulo':'Underworld','productor':'Len Wiseman','año':'2003'},
    '004' : {'titulo':'Crepusculo','productor':'Catherine Hardwicke','año':'2008'}
}

def nueva_pelicula():
    id_pelicula = input("Ingrese el ID de la pelicula: \n")
    if id_pelicula in bibliotecaPeliculas:
        print("Este ID ya existe. Intente con otro.")
        return
    titulo = input("Ingrese el titulo de la pelicula")
    productor = input("Ingrese el autor del libro: \n")
    try:
        año = int(input("Ingrese el año de estreno de la pelicula: \n"))
    except ValueError:
        print(f"El año debe ser un numero entero.")
        return
    bibliotecaPeliculas[id_pelicula]={'titulo':titulo,'productor':productor,'año':año}
    print("Pelicula agregada exisitosamente.")
       
def ver_pelicula():
    if not bibliotecaPeliculas:
        print("No hay peliculas en la biblioteca.")
        return
    print("\nListado de peliculas: ")
    for id_pelicula , info in bibliotecaPeliculas.items():
        print(f"ID: {id_pelicula}, Titulo: {info['titulo']}, Productor: {info['productor']}, Año: {info['año']}")

def buscar_pelicula():
    criterio = input("""¿Buscar por ID o por titulo?
Escriba 'id' o 'titulo'\n""")
    if criterio == 'id':
        id_buscar = input("Ingrese el Id de la pelicula")
        pelicula = bibliotecaPeliculas.get(id_buscar)
        if pelicula:
            print(f"Titulo: {pelicula['titulo']}, Autor: {pelicula['productor']}, Año: {pelicula['año']}")
        else:
            print("Pelicula no encontrada")
    elif criterio == 'titulo':
        titulo_buscar = input("Ingrese el titulo de la pelicula: ").strip().lower()
        encontrado = False
        for info in bibliotecaPeliculas.values():
            if info['titulo'].lower() == titulo_buscar:
                print(f"Titulo: {pelicula['titulo']}, Autor: {pelicula['productor']}, Año: {pelicula['año']}")
                encontrado = True
                break
        if not encontrado:
            print("Pelicula no encontrada")