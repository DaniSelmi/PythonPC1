time = input("hora ")
hours,minutes = time.split(":")
hours = float(hours)

if 7 <= hours <= 8:
    print("Es la hora del desayuno")
elif 12 <= hours <= 13:
    print("Es la hora del almuerzo")
elif 18 <= hours <= 19:
    print("Es la hora de la cena")
