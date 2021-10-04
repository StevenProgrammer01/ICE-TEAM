# Prototipo de como funciona el algoritmo de alerta de estrés térmico

import ast
import urllib.request

def temperatura_ciudad(id_ciudad): # Función para sacar datos de la API
    URL_weather = "http://api.openweathermap.org/data/2.5/weather?id="+str(id_ciudad)+"&appid=a0a54f12f7002192685452906efbb8ba"
    weather_data = urllib.request.urlopen(URL_weather).read()
    weather_data = ast.literal_eval(weather_data.decode('utf-8'))
    return weather_data["main"]["temp"]-273.15

def Recomendacion(temp): #Función para determinar el nivel de estrés térmico
    if temp >= 40.0: #Grados Celsius
        print(Lugar0, "Esta en condición Roja de acuerdo a la escala de estrés térmico con una temperatura de=",'%.1f' %temp,"C \n"
                     "Le recomendamos seguir estas medidas:\n"
                     "1.Si presenta mucho sudor, cansancio, piel irritada, sed, \n"
                     "tome un descanso a la sombra he hidrátese\n"
                     "2.Use bloqueador solar y si sale lleve protección para la piel\n"
                     "3.Use sombrero y ropa holgada que proteja su piel\n"
                     "4.Tomar un vaso de agua cada 15 minutos cerca de las horas de más calor\n"
                     "5.No trabaje expuesto al sol entre las 10 am y las 4 pm\n"
                     "6.Aliméntese adecuadamente\n"
                     "7.Haga trabajo de intensidad baja, sobre todo cerca de las horas de más calor")


    elif temp < 40.0 and temp >= 30.0:
        print(Lugar0, "Esta en condición Amarilla de acuerdo a la escala de estrés térmico con una temperatura de=",'%.1f' %temp,"C \n"
                     "1.Si presenta mucho sudor, cansancio, piel irritada, sed, \n"
                     "tome un descanso a la sombra he hidrátese\n"
                     "2.Use bloqueador solar y si sale lleve protección para la piel\n"
                     "3.Use sombrero y ropa holgada que proteja su piel\n"
                     "4.Tome un vaso de agua aproximadamente cada 30 minutos cerca de las horas de más calor\n"
                     "5.No trabaje expuesto al sol entre las 10 am y las 3 pm.\n"
                     "6.Haga trabajo de intensidad moderada, sobre todo cerca de las horas de más calor")


    elif temp < 30.0:
        print(Lugar0, "Esta en condición Verde de acuerdo a la escala de estrés térmico con una temperatura de=",'%.1f' %temp,"C \n"
                     "1.Si presenta mucho sudor, cansancio, piel irritada, sed, \n"
                     "tome un descanso a la sombra he hidrátese\n"
                     "2.Use bloqueador solar y si sale lleve protección para la piel\n"
                     "3.Use sombrero y ropa holgada que proteja su piel\n"
                     "4.Tome agua aproximadamente 2 litros al día\n"
                     "5.No trabaje expuesto al sol entre las 11 am y las 3 pm")


Liberia = 3623076 #Lista ciudades de Guanacaste por código para buscar en API
Nicoya = 3622716
SantaCruz = 3621607
Belen = 3624718
Sardinal = 3621490
Hojancha = 3623454
Bagaces = 3624822
Cañas = 3624468
LaCruz = 3623258
Carrillo = 3624379
Nandayure = 3622765


Lugar0 = input("Agregue el distrito guanacasteco del que quieres saber: ")
Lugar = Lugar0.lower()
Lugar = Lugar.replace(" ", "")

Lista = [Liberia, Nicoya, SantaCruz, Belen, Sardinal, Hojancha, Bagaces, Cañas, LaCruz, Carrillo, Nandayure]

#Lista de if donde integro las funciones y las ejecuto

if Lugar == "liberia":
    Recomendacion(temperatura_ciudad(Lista[0],))

elif Lugar == "nicoya":
    Recomendacion(temperatura_ciudad(Lista[1],))

elif Lugar == "santacruz":
    Recomendacion(temperatura_ciudad(Lista[2],))

elif Lugar == "belen":
    Recomendacion(temperatura_ciudad(Lista[3],))

elif Lugar == "sardinal":
    Recomendacion(temperatura_ciudad(Lista[4],))

elif Lugar == "hojancha":
    Recomendacion(temperatura_ciudad(Lista[5],))

elif Lugar == "bagaces":
    Recomendacion(temperatura_ciudad(Lista[6],))

elif Lugar == "cañas":
    Recomendacion(temperatura_ciudad(Lista[7],))
elif Lugar == "lacruz":
    Recomendacion(temperatura_ciudad(Lista[8],))
elif Lugar == "carrillo":
    Recomendacion(temperatura_ciudad(Lista[9],))
elif Lugar == "nandayure":
    Recomendacion(temperatura_ciudad(Lista[10],))

else:
    print("Lo sentimos el lugar que ingreso no está disponible, o escriba el nombre correctamente")


