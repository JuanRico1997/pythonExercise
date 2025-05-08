peliculas = {
    '001' : {'Nombre': "Harry Potter",'Autor' : 'JJ K','Año': '2010'},
    '002' : {'Nombre': "El señor de los anillos",'Autor' : 'Tolking K','Año': '1010'}
}

usuarios = {
    'sergio': {
        'photos': ['photo.1', 'photo.2'],    
        'historial_busqueda': ['google', 'youtube']
    },
    'juan': (0, 0, 0, ),
    'camila': {}
}

print(usuarios.get("sergio")['photos'][0])

print(peliculas.get('001'))

peli = input("Ingrese  id de la pelicula a buscar:  ")



if peliculas.get(peli):
    print(peliculas.get(peli))
else:
    print("No se encuentra")

