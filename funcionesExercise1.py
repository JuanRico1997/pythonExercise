sume = 0
students = []
def data():
    name = input("Ingrese nombre del estudiante: ")
    grades=[]
    for i in range(3):
        while True:
            try:
                grade = float(input(f"Ingrese la nota {i+1} del estudiante: "))
                while True:
                    if grade == 0 or grade <= 5.0:
                        grades.append(grade)
                        break
                    else:
                        print("Ingrese una nota entre 0 - 5")
                        grade = float(input(f"Ingrese la nota {i+1} del estudiante: "))
                
                break
            except ValueError:
                print("Ingrese un valor numerico")
    students.append({"Nombre":name,"Notas":grades})
    print(f"El estudiante {name} fue agregado exitosamente")
    
def notes():
    
    for posicion, student in enumerate(students):
        average = sum(students[posicion]["Notas"])/len(students[posicion]["Notas"])
        students[posicion]['Promedio'] = average
        print(f"El promedio de {student['Nombre']} es: {average:.2f}")     
        if average>=3.0:
            print("Aprobó la materia.")
        else:
            print("Reprobó la materia.")
    print(students)
        

while True:
    try:
        cantstudents = int(input("Ingrese la cantidad de estudiantes: "))
        break
    except ValueError:
        print("Solo se pueden numeros enteros")
i=0
while i<cantstudents:

    data()
    notes() 
    i+=1

