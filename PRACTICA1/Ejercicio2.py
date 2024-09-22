# Solicitar el consumo en el restaurante
consumo = float(input("¿Cuánto fue tu consumo en el restaurante? "))

# Solicitar el porcentaje de propina que desea dejar
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar? "))

# Calcular la propina
propina = consumo * (porcentaje_propina / 100)

# Mostrar la cantidad de dinero a dejar como propina
print(f"La cantidad de propina a dejar es: ${propina:.2f}")