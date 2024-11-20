# 01
def calcular_promedio(notas):
    suma = 0
    for i in range(notas):
        nota = int(input("Ingrese su nota: "))
        suma += nota
    return suma / notas

nota_general = calcular_promedio(3)
print(f"Su calificacion general es: {nota_general}")

# 02
""" def es_primario(color):
    color = color.lower()
    if color == "rojo" or color == "verde" or color == "azul":
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")

es_primario("AZUL") """

# 03
""" def determinar_mayor(numeros):
    if len(numeros) == 0:
        print("ERROR: No ingresó numeros")
    else:
        return max(numeros)

mayor = determinar_mayor([1, 2, 3, 4, 5, 9])
print(f"El mayor de los numeros es: {mayor}") """


# 04
""" def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        for j in range (columnas):
            print("*", end=" ")
        print()

dibujar_rectangulo(5, 7) """


# 05
""" def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

factorial = calcular_factorial(5)
print(factorial) """