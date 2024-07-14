opciones = print("""
MENÚ:
1) Suma de los dos números (a+b)
2) Resta de los dos números (a-b)
3) Multiplicación de los dos números (a*b)

Escoger una de las 3 opciones               
""")

opcion = int(input("Opción seleccionada es: "))

if opcion == 1:
    a = float(input("valor de 'a' es: "))
    b = float(input("valor de 'b' es: "))
    resultado = a + b
    print(f"El resultado es {resultado}")

elif opcion == 2:
    a = float(input("valor de 'a' es: "))
    b = float(input("valor de 'b' es: "))
    resultado = a - b
    print(f"El resultado es {resultado}")

elif opcion == 3:
    a = float(input("valor de 'a' es: "))
    b = float(input("valor de 'b' es: "))
    resultado = a * b
    print(f"El resultado es {resultado}")
    
else:
    print("La opción es inválida")


