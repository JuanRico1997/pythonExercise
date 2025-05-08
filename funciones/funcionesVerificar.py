#Funcion para verificar un dato y doble validacion por si se necesita otra que cumpla otro requisito
def verifyInput(msg, type=str, extraValidation=None, extraErrorMsg="Error"):
    while True:
        response = input(msg).strip()
        try:
            value = type(response)
            if extraValidation and not extraValidation(value):
                print(f"{extraErrorMsg}")
                continue
            return value
        except ValueError:
            print(f"Entrada inválida. Ingresa un valor del tipo {type.__name__}.")
            
            