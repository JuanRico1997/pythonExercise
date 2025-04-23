palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador = 0 
for letra in palabra:
    if letra in vocales:
        contador = contador + 1

print("Tiene " , contador , " vocales ") 