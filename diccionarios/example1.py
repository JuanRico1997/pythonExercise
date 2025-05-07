users = [
    {   "cc":123,
        "nombre":"Juan",
        "apellido":"Rico",
        "edad":25,
        "telefono":"3011920031"
    },
     {
        "cc":354,
        "nombre":"Ana",
        "apellido":"Zapata",
        "edad":35,
        "telefono":"3017724031"
    },
      {
        "cc":456,
        "nombre":"Jorge",
        "apellido":"Rico",
        "edad":51,
        "telefono":"3105076452"
    },
      {
        "cc":654,
        "nombre":"Juan",
        "apellido":"Rico",
        "edad":25,
        "telefono":"3011920031"
    }
]

new_user =  {
        "cc":545,
        "nombre":"Liliana",
        "apellido":"Yepes",
        "edad":49,
        "telefono":"3085202368"
    }

users.append(new_user)
print(users)

#buscar un usuario por nombre

for i in users:
    if i["nombre"].lower() == "Ana".lower():
        print(i)
        break
    
for i in users:
    if i["apellido"].lower() == "zapata".lower():
        print(i["edad"])
        
#Modificar un dato de un diccionario de una lista

for user in users:
    if user["nombre"].lower()== "liliana".lower():
        user["edad"] = 55
        print(user["edad"])
        
#Eliminar un dato de una lista

for i in users:
    if i["cc"]==654:
        users.remove(i)
        break

print(users)

#TUPLASSSSS

isActive = False
tupla=(45678,"Administrador")

user = input("Ingrese user")
password = input("Ingrese passWord")

if user == tupla[1] and password==tupla[0]:
    
    print("Ha ingresado: ")
else:
    print("Datos incorrectos: ")

