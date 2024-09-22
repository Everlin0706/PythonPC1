# Solicitar al usuario que ingrese cuántos shows musicales ha visto en el último año
num_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Verificar si el número de shows es mayor que 3
ha_visto_mas_de_tres = num_shows > 3

# Mostrar el valor booleano correspondiente
print(ha_visto_mas_de_tres)