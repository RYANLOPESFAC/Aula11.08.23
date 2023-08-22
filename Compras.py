def listar_itens(lista):
    print("Itens na lista de compras:")
    for idx, item in enumerate(lista, start=1):
        print(f"{idx}. {item}")

def adicionar_item(lista, item):
    lista.append(item)
    print(f"{item} foi adicionado à lista de compras.")

def remover_item(lista, indice):
    if 1 <= indice <= len(lista):
        item_removido = lista.pop(indice - 1)
        print(f"{item_removido} foi removido da lista de compras.")
    else:
        print("Índice inválido. Nenhum item foi removido.")

def editar_item(lista, indice, novo_item):
    if 1 <= indice <= len(lista):
        lista[indice - 1] = novo_item
        print(f"Item {indice} foi atualizado para {novo_item}.")
    else:
        print("Índice inválido. Nenhum item foi atualizado.")

def main():
    lista_de_compras = []

    while True:
        print("\nMenu:")
        print("1. Listar itens")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Editar item")
        print("5. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            listar_itens(lista_de_compras,) 
        elif escolha == 2:
            item = input("Digite o novo item: ")
            adicionar_item(lista_de_compras, item)
        elif escolha == 3:
            listar_itens(lista_de_compras)
            indice = int(input("Digite o índice do item a ser removido: "))
            remover_item(lista_de_compras, indice)
        elif escolha == 4:
            listar_itens(lista_de_compras)
            indice = int(input("Digite o índice do item a ser editado: "))
            novo_item = input("Digite o novo valor do item: ")
            editar_item(lista_de_compras, indice, novo_item)
        elif escolha == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

