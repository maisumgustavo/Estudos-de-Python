
tarefasConcluidas = []
tarefas = []

while True:
    print('\nO que deseja fazer?')
    print('1 - Adicionar tarefa.')
    print('2 - Trocar tarefa.')
    print('3 - Remover tarefa.')
    print('4 - Concluir tarefa.')
    print('5 - Listar tarefas.')
    print('6 - Listar tarefas concluidas.')
    print('7 - Sair')

    opcao = int(input())

    if opcao == 1:
        tarefas.append(str(input('Adicione a tarefa: \n')))

    elif opcao == 2:
        print(tarefas)
        opcao = str(input('Escolha a terfa que você quer trocar. \n'))
        if opcao in tarefas:
            id = tarefas.index(opcao)
            tarefas.remove(opcao)
            opcao = str(input('Qual a nova tarefa? '))
            tarefas.insert(id, opcao)
            print(tarefas)

        else:
            opcao = str(input('Item não encontrado ou com nome errado, pode escrever de novo? \n'))
            id = tarefas.index(opcao)
            tarefas.remove(opcao)
            opcao = str(input('Qual a nova tarefa? \n'))
            tarefas.insert(id, opcao)
            print(tarefas)

    elif opcao == 3:
        id = tarefas.index(opcao)
        tarefas.remove(opcao)

    elif opcao == 4:
        print(tarefas)
        opcao = str(input('Qual tarefa você concluiu? '))
        id = tarefas.index(opcao)
        tarefasConcluidas = tarefas[id]
        tarefas.remove(opcao)
        print(tarefasConcluidas)

    elif opcao == 5:
        print(tarefas)

    elif opcao == 6:
        print(tarefasConcluidas)

    else:
        print('Saindo...')
        break
