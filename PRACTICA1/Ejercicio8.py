# Solicitar la hora al usuario
time = input("Ingrese la hora en formato H:MM o HH:MM: ")

# Separar horas y minutos
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

# Convertir la hora a formato flotante
time_float = hours + minutes / 60

# Verificar en qué rango cae la hora
if 7 <= time_float <= 8:
    print("Es la hora del desayuno.")
elif 12 <= time_float <= 13:
    print("Es la hora del almuerzo.")
elif 18 <= time_float <= 19:
    print("Es la hora de la cena.")