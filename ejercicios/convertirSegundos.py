segundos = int (input("Ingrese la cantidad de segundos a convertir: "))

h = segundos // 3600
moduloHoras = segundos % 3600
m = moduloHoras // 60
s = moduloHoras % 60




print("Hr:",h , "Min: " , m , "Segundos: ",  s )