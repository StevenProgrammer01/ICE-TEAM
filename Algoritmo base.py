# Algoritmo base


#Este eran los comienzos del code

def Calculo(Lugar, Dia, Mes):
    Dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31]
    Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    if Lugar == "Costa Rica" and Dia == Dias[0] and Mes == Meses[0]:
        print("El lugar que escogiste ese día a esa hora está muy caliente.\n"
              "Recomendamos siga las siguientes medidas:\n"
              "bla bla\n"
              "bla bla\n"
              "bla bla")


Lugar = input("Ingresa el lugar: ")
Dia = int(input("Ingresa el día: "))
Mes = input("Ingresa el mes: ")


List = [Lugar, Dia, Mes]

Calculo(List[0], List[1], List[2])


