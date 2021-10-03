# Prototipo de como funciona el algoritmo de alerta de estrés térmico

def calc(Lista):
    if Lista >= 40:
        print(Lugar, "Esta en condición Roja de acuerdo a la escala de estrés térmico\n"
                     "Le recomendamos seguir estas medidas:\n"
                     "No estar más de 30 minutos bajo el sol\n"
                     "Use bloqueador solar y si sale lleve protección para la piel\n"
                     "Tome agua aproximadamente 2 litros al día\n"
                     "Recuerde que las horas más calientes son al medio día")


    elif Lista < 40 and Lista >= 30:
        print(Lugar, "Esta en condición Amarillo de acuerdo a la escala de estrés térmico\n"
                     "Le recomendamos seguir estas medidas:\n"
                     "No estar más de 1 hora bajo el sol\n"
                     "Use bloqueador solar y si sale lleve protección para la piel\n"
                     "Tome agua aproximadamente 2 litros al día\n"
                     "Recuerde que las horas más calientes son al medio día")

    elif Lista < 30:
        print(Lugar, "Esta en condición Verde de acuerdo a la escala de estrés térmico\n"
                     "Le recomendamos seguir estas medidas:\n"
                     "Puede estar bajo el sol no más de 5 horas\n"
                     "Use bloqueador solar y si sale lleve protección para la piel\n"
                     "Tome agua aproximadamente 2 litros al día\n"
                     "Recuerde que las horas más calientes son al medio día")


Liberia = 27
Nicoya = 35
SantaCruz = 40
Belen = 39
Sardinal = 41
Hojancha = 29

Lugar = input("Agregue el distrito guanacasteco del que quieres saber: ")
Lugar = Lugar.lower()


Lista = [Liberia, Nicoya, SantaCruz, Belen, Sardinal, Hojancha]

if Lugar == "liberia":
    calc(Lista[0])

elif Lugar == "nicoya":
    calc(Lista[1])

elif Lugar == "santa cruz":
    calc(Lista[2])

elif Lugar == "belen":
    calc(Lista[3])

elif Lugar == "sardinal":
    calc(Lista[4])

elif Lugar == "hojancha":
    calc(Lista[5])

else:
    print("Lo sentimos el lugar que ingreso no está disponible, o escriba el nombre correctamente")
