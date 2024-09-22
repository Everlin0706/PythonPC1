# Definir el peso de cada payaso y muñeca en gramos
peso_payaso = 112
peso_muneca = 75

try:
    # Solicitar la cantidad de payasos y muñecas vendidos
    num_payasos = int(input("Introduce el número de payasos vendidos: "))
    num_munecas = int(input("Introduce el número de muñecas vendidas: "))

    # Calcular el peso total del paquete
    peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

    # Mostrar el peso total del paquete
    print(f"El peso total del paquete es: {peso_total} gramos.")

except ValueError:
    print("Por favor, introduce un número válido para la cantidad de payasos y muñecas.")
    