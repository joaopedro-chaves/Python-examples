# Manipulação de listas (Arrays and Lists manipulation) e Menu de opções (Terminal menu)

# lista de nomes - Array/List
names = ['Ana', 'Bruno', 'Carlos', 'Daniel', 'Eva', 'Fernanda']

# Seleção de função em python (selecionar a opção que deseja usar)

listFunctions = """
Funções disponíveis:
1. Exibir lista de nomes
2. Adicionar 1 nome
3. Adicionar 2 nomes
4. Adicionar mais nomes com while
5. Remover 1 nome
6. Remover ultimo nome
7. Pesquisar 1 nome na lista
8. Sair
"""

print(listFunctions)

# Loop infinito - Execução do progama até que o usuário digite "5"
while True:
    opcao = input("Digite a opção desejada (0 para ver as opções): ").lower()
    
    if opcao == "0": # Exibe a lista de funções
        print(listFunctions)
    elif opcao == "1": # Exibe a lista de nomes
        print(f"Lista de nomes: {names}")
    elif opcao == "2": # Adiciona 1 nome
        names.append(input("Digite um nome: "))
        print(f"Lista de nomes atualizada: {names}")
    elif opcao == "3": # Adiciona 2 nomes
        for i in range(2):
            names.append(input(f"Digite o {i+1}º nome: "))
            print(f"Lista de nomes atualizada: {names}")
    elif opcao == "4": # Adiciona mais nomes com while
        while input("Deseja adicionar um nome? (s/n): ").lower() == "s":
            names.append(input("Digite um nome: "))
            print(f"Lista de nomes atualizada: {names}")
    elif opcao == "5": # Remove 1 nome
        names.remove(input("Digite o nome que deseja remover: "))
        print(f"Lista de nomes atualizada: {names}")
    elif opcao == "6": # Remove o ultimo nome
        names.pop()
        print(f"Último nome removido")
        print(f"Lista de nomes atualizada: {names}")
    elif opcao == "7": # Pesquisa 1 nome na lista
        nameSearch = input("Digite o nome que deseja pesquisar: ")
        if nameSearch in names:
            print(f"Nome {nameSearch} encontrado na lista")
        else:
            print(f"Nome {nameSearch} não encontrado na lista")
    elif opcao == "8": # Sai do programa
        break
    else:
        print("Opção inválida")