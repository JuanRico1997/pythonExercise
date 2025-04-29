def aprobarNota():
    while True:
        note = input("Ingrese nota: ")
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
    acumulator = 0
    acumulator2 = 0

    print("-----MENÚ PRINCIPAL-----")
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

        cantNote = input("Cuantas notas desea ingresar?\n")
        while not cantNote.isnumeric():
                print("No se permite caracteres ni numeros decimales.")
                cantNote = input("\nCuantas notas desea ingresar?\n")
        for i in range(1,int(cantNote)+1):
            notas = int (input(f"Ingrese sus nota {i}:"))
            listNote.insert(i,notas)
            
        
        print("El promedio de sus notas es: ",promedioNotas(listNote))
        print (f"Las notas son: {listNote}\n")

    elif int(option) == 3:
        cont1=0
        cantNote = input("Cuantas notas desea ingresar?\n")
        while not cantNote.isnumeric():
            print("No se permite caracteres ni numeros decimales.")
            cantNote = input("\nCuantas notas desea ingresar?\n")
        for i in range(1,int(cantNote)+1):
            notas = int (input(f"Ingrese sus nota {i}:"))
            listNote.insert(i,notas)
        especificValue = input("Ingrese un valor especifico: ")
        for i in range(0,int(cantNote)):
            if int(listNote[i])>=int(especificValue):
                cont1+=1
        print (f"Las notas son: {listNote}\n")
        print("Las notas mayores al valor especifico ingresado son: ",cont1)

    elif int(option) == 4:
        
        note = input("Ingrese las notas separadas por coma: ").split(",")
        notes = list(map(int,note))      
        promedio = sum(notes)/len(notes)
        print(f"Las notas son {notes} y el promedio es {promedio}")

    print("\nDesea volver al menú?")
    menu = int(input("""
1.Si
2.No\n"""))
    if menu == 1:
        iniciar = True
    else:
        break





    
        



        




