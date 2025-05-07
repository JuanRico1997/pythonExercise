def aprobarNota():
    while True:
        note = input("Ingrese nota --- Debe ser de 0 a 100\n")
        
        if not note.isnumeric():
            print("No se permite caracteres.")
            continue
        elif int(note)<0 or int(note)>100:
            print("Ingrese una nota en el rango especificado")
            continue

        if int(note)<60:
            print("Perdio la nota.")
            break
        else:
            print("Gano la nota")
            break


def promedioNotas(n):
    return sum(n)/len(n)

iniciar = True



while iniciar:
    listNote = []
    
    print("-----MENÚ PRINCIPAL-----")
    option = input("""Ingrese una opcion:
    1.Determinar el estado de aprobación
    2.Calcular el promedio
    3.Contar calificaciones mayores
    4.Verificar y contar calificaciones específicas\n""")

    while int(option)>5 or int(option)<1:
        
        option = input("""Ingrese una opcion:
    1.Determinar el estado de aprobación
    2.Calcular el promedio
    3.Contar calificaciones mayores
    4.Verificar y contar calificaciones específicas\n""")

    while not option.isnumeric():
        print ("Ingrese una Opcion valida")
        option = input("""
    1.Determinar el estado de aprobación
    2.Calcular el promedio
    3.Contar calificaciones mayores
    4.Verificar y contar calificaciones específicas\n""")
        

    if int(option) == 1:

        aprobarNota()

    elif int(option) == 2:

        quantityNote = input("Cuantas notas desea ingresar?\n")
        while not quantityNote.isnumeric():
                print("No se permite caracteres ni numeros decimales.")
                quantityNote = input("\nCuantas notas desea ingresar?\n")
            
        for i in range(1,int(quantityNote)+1):
            while True:
                try:
                    notas = int(input(f"Ingrese sus nota {i}:"))
                    while int(notas)<0 or int(notas)>100:
                        print("Ingrese la nota en el rango estipulado")
                        notas = (input(f"Ingrese sus nota {i}:"))
                    listNote.insert(i,int(notas))
                    break
                except ValueError:
                    print("Solo se permiten numeros enteros")
        print(listNote)    
        print (f"Las notas son: {listNote}\n")
        print("El promedio de sus notas es: ",promedioNotas(listNote))
        

    elif int(option) == 3:
        accountant=0
        quantityNote = input("Cuantas notas desea ingresar?\n")
        while not quantityNote.isnumeric():
            print("No se permite caracteres ni numeros decimales.")
            quantityNote = input("\nCuantas notas desea ingresar?\n")
        for i in range(1,int(quantityNote)+1):
            notes = input(f"Ingrese sus nota {i}:")
            while not notes.isnumeric():
                print("Solo se permiten numeros enteros")
                notes = (input(f"Ingrese sus nota {i}:"))
            listNote.insert(i,int(notes))
        especificValue = input("Ingrese un valor especifico: ")
        while not especificValue.isnumeric():
            print("No se permiten caracteres ni numeros decimales")
            especificValue = input("Ingrese un valor especifico: ")
        for i in range(0,int(quantityNote)):
            if int(listNote[i])>int(especificValue):
                accountant+=1
        print (f"Las notas son: {listNote}\n")
        print("Las notas mayores al valor especifico ingresado son: ",accountant)

    elif int(option) == 4:
        while True:
            try:
                accountant = 0
                note = input("Ingrese las notas separadas por coma: ").split(",")
                notes = list(map(int,note))
                if any(i < 0 or i>100 for i in notes):
                    print("Las notas deben ser de 0 --- 100")
                    continue
                average = sum(notes)/len(notes)
                print(f"Las notas son {notes} y el promedio es {average}")
                repetitions = input("Ingrese un numero a verificar si se repite: ")
                for i in range(0,len(notes)):
                    if int(repetitions) == notes[i]:
                        accountant+=1
                print(f"El numero se repite {accountant} veces.")
                break
            except ValueError:
                print("No se perimiten caracteres")
                
    else:
        print("Ingrese una opción valida.")
        
    print("\nDesea volver al menú?")
    menu = int(input("""
1.Si
2.No\n"""))
    if menu == 1:
        iniciar = True
    else:
        break





    
        



        




