# Solicitar dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar el menú de opciones
print("\nElige una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")

# Solicitar al usuario que elija una opción
opcion = int(input("\nIntroduce tu opción (1/2/3): "))

# Realizar la operación seleccionada y mostrar el resultado
if opcion == 1:
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")
elif opcion == 2:
    print(f"La resta de {num1} menos {num2} es: {num1 - num2}")
elif opcion == 3:
    print(f"La multiplicación de {num1} por {num2} es: {num1 * num2}")
else:
    print("Opción no válida. Por favor, elige una opción correcta.")