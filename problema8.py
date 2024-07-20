time = input("hora ")
hours,minutes = time.split(":")
hours = float(hours)

if 7 <= hours <= 8:
    print("Es la hora del desayuno")
elif 12 <= hours <= 13:
    print("Es la hora del almuerzo")
elif 18 <= hours <= 19:
    print("Es la hora de la cena")

#Otra forma

respuesta = input("Que hora es? ")
respuesta = respuesta.lower().strip()

hora, minuto = respuesta.split(":")

h = float(hora) + int(minuto)/60

if 7<_= h <=8:
    print("breakfast time")
elif 12<= h <=13:
    print("lunch time")
elif 18<= h <=19:
    print("dinner time")


