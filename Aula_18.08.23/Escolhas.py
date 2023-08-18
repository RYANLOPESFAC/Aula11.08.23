opcao = int(input('escolha uma opção:\n1 - Maçã\n2 - Banana\n3 - Laranja\nOpção'))

if opcao == 1:
    print('Você escolheu Maçã.')
elif opcao == 2:
    print('Você escolheu Banana.') 
elif opcao == 3:
    print('Você escolheu Laranja.') 
else:
    print('Opção inválida.')          

    contador = 1 

while contador <= 5:
    print("Contador:",contador)
    contador = contador + 1

for conrtador in range(1, 6):
    print('Contador:', contador)    
    