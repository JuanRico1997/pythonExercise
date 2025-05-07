import random

number = random.randint(1,10)

intentos = 0

while True:
    
    adivinar = int(input("Adivina el numero !!!!\n"))

    if adivinar == number:
        print(f"Adivinaste el numero !! en {intentos} intentos")
        break
    else:
        "Sigue intentando"
        intentos+= 1

print("El numero era ", number)        
    

    
    
    



    
