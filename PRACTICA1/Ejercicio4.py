# Solicitar al usuario que ingrese un entero positivo
n = int(input("Introduce un número entero positivo: "))

if n > 0:
    # Calcular la suma de los primeros N enteros positivos usando la fórmula
    suma = n * (n + 1) // 2
    
    # Mostrar el resultado
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")
else:
    print("Por favor, introduce un número entero positivo válido.")