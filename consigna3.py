M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]

print("Promedio por función:")

for fila in M:
    promedio = sum(fila) / len(fila)
    print(promedio)

print("\nPromedio por servidor:")

for columna in range(3):
    suma = 0

    for fila in range(3):
        suma += M[fila][columna]

    promedio = suma / 3
    print(promedio)

print("\nMatriz transpuesta:")

for columna in range(3):

    for fila in range(3):
        print(M[fila][columna], end=" ")

    print()

print("\nProducto M * C:")

T = []

for i in range(3):

    fila_resultado = []

    for j in range(3):

        suma = 0

        for k in range(3):
            suma += M[i][k] * C[k][j]

        fila_resultado.append(suma)

    T.append(fila_resultado)

for fila in T:
    print(fila)