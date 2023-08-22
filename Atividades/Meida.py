
alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    alunos[nome] = nota

soma_notas = sum(alunos.values())  
media = soma_notas / len(alunos)    

print("\nNotas dos Alunos:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

print("\nMédia das Notas:", media)
