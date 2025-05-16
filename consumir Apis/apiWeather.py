import urllib.request
import json
import datetime



def obtenerClimas(ciudad,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    print(url)
    with urllib.request.urlopen(url) as response:
        data= response.read()
        print(data)
        jsonData = json.loads(data)
        # print(jsonData)
        return  jsonData
while True:
        
    city = input("Ingrese la ciudad que desea conocer su clima: ")
    resultado = obtenerClimas(city,"eea07ff56be273ff796014770046c5ed")
    print(f"Clima:{resultado['weather'][0]['description']}")
    if resultado['main']['temp'] < 0:
        print(f"Temperatura:{resultado['main']['temp']}°C \U00002744 ")
    elif resultado['main']['temp'] > 0 and resultado['main']['temp'] < 10 :
        print(f"Temperatura:{resultado['main']['temp']} °C \U0001F327 ")
    elif resultado['main']['temp'] >= 10 and resultado['main']['temp'] < 18 :
        print(f"Temperatura:{resultado['main']['temp']}°C \u26C5 ")
    else:
        print(f"Temperatura:{resultado['main']['temp']} \U00002600 ")
    print(f"Humedad: {resultado['main']['humidity']}")
    print(f"Velocidad del viento: {resultado['wind']['speed']}")
    print(f"País: {resultado['sys']['country']}")
    sunrise = datetime.datetime.fromtimestamp(resultado['sys']['sunrise'])
    print(f"Amanecer:{sunrise}")
    print(sunrise)
    
    
    
    