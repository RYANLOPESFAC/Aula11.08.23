numeros = []  

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


soma = 0  

for numero in numeros:
    soma += numero

print("\nNúmeros digitados:", numeros)
print("Soma dos números:", soma)
