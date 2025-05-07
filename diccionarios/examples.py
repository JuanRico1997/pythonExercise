numbers = {
    1:"uno",
    2:"dos",
    3:{
        "nombre":"david",
        "cc":1036673236    
    },
    4:"cuatro",
    5:"cinco"
}

# Imprimir o acceder a un valor especifico
# print(numbers[4])

# print(f"{numbers[3]["cc"]}")

informacion = {
    "nombre":"Juan",
    "apellido":"Perez",
    "edad":25,
    "telefono":"3011920031"
    
}

# modificar datos

informacion["edad"]=30

print(informacion)

#Agregar nueva clave

informacion["cc"]="1036673236"
print(informacion)

#Eliminar clave

del informacion["telefono"]
print(informacion)

#Mostrar las claves y values

print(informacion.keys())
print(informacion.values())