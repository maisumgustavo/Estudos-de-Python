import Todo_Db

MENU_INICIAL = 99


def exibir_cabecalho():
    """Imprimi o cabeçalho no terminal utilizando o tamanho máximo de 60 caracteres"""
    QTD_COLUNAS = 60
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("TAREFAS"))
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("tecle 99 volta para o menu inicial, [Ctrl+C] sai"))
    print("-" * QTD_COLUNAS)


def exibir_tarefas():
    """Exibe a lista de tarefas cadastradas, com algumas formatações básicas"""
    for tarefa in Todo_Db.listar_tarefas():
        check = u'\u2713' if tarefa[2] == 1 else ""
        lista_tarefas = "- [{:>4}] {:<47} {:^3}".format(tarefa[0], tarefa[1], check)
        print(lista_tarefas)
    print("-" * 60)


def mostrar_opcao_nova_tarefa():
    nova_tarefa = input("Digite a nova tarefa: ")
    print("Adicionando nova tarefa => " + str(nova_tarefa))
    if nova_tarefa != str(MENU_INICIAL):
        Todo_Db.adicionar_tarefa(nova_tarefa)
    print("Tarefa adicionada!")


def mostrar_opcao_concluir_tarefa():
    id_tarefa = int(input("Qual o número da tarefa que quer concluir: "))
    print("Concluindo tarefa => " + str(id_tarefa))
    if id_tarefa != MENU_INICIAL:
        Todo_Db.concluir_tarefa(id_tarefa)
    print("Tarefa concluída!")
