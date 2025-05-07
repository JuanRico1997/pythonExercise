def convertir_a_Usd (pesosCol,tasa):
    usd = pesosCol/tasa
    return usd


pesosCol = float(input("Ingrese COP: "))
tasa = float(input("Ingrese la tasa del dia de hoy: "))

print(convertir_a_Usd(pesosCol,tasa))