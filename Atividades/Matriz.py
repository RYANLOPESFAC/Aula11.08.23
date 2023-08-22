name 'np' is not defined
Ryan_matriz = np.array([[3, 4, 1], [3, 2, 1]])

soma_total = 0


for linha in Ryan_matriz:
    for elemento in linha:
        soma_total += elemento

print("Matriz:")
print(Ryan_matriz)

print("\nSoma total dos elementos:", soma_total)
