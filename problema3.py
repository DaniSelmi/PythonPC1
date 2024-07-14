peso_payaso = 112
peso_muñeca = 75

n_payasos_vendidos = int(input("Cuantos payasos se vendio: "))
n_muñecas_vendidos = int(input("Cuantos muñecas se vendio: "))

peso_total = peso_payaso*n_payasos_vendidos + peso_muñeca*n_muñecas_vendidos

print(f"El peso total del paquete es {peso_total}")
