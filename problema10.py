lista_muestra = ['Rojo','Verde','Blanco','Negro','Rosa','Amerrillo']
del lista_muestra[4:6]
del lista_muestra[0]
print(lista_muestra)

#OTRA FORMA
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
l0 = lista[0]
l4 = lista[4]
l5 = lista[5]
lista.remove(l0)
lista.remove(l4)
lista.remove(l5)
print(lista)