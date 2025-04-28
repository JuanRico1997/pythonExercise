listNote = []

# print("Desea ingresar una nota ?")
# regNote = input("""Oprima
# 1.Si desea ingresar nota 
# 2.No desea ingresar nota\n""")

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



# while int(regNote) == 1:

#     quantityNote = int(input("Ingrese cuantas notas desea registar:\n "))
#     print("TEN MUY PRESENTE !!!!!!")
#     print("El rango de la nota debe ser entre 0 - 100")

#     for i in range(1,quantityNote+1):
        
#         while True:

#             note = input(f"Ingrese nota {i}: ")
#             if not note.isnumeric():
#                 print("No se permite caracteres.")
#                 continue
#             elif int(note)<0 or int(note)>100:
#                 print("Ingrese una nota en el rango especificado")
#                 continue
#             else:
               
#                 listNote.insert(i,note)
#                 break
        
              

#     regNote = input("Oprima 1.Si desea ingresar nota 2.No desea ingresar nota: ")


# print (f"Las notas son: {listNote}")
        



        




