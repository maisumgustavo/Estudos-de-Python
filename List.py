
nomes = []

def adicionarItems():
    nomes.append(str(input('Por favor, escreva um nome: ')))

def removerItems():
    nomes.pop()

def listar():
    print(nomes)

while True:
    opcao = int(input('Deseja: 1 - Adicionar um item, 2 - Remover um item, 3 - Mostrar items, 4 - Sair'))
    
    if opcao == 1:
        adicionarItems()
    
    elif opcao == 2:
        removerItems()
        print('Item removido.')
    
    elif opcao == 3:
        listar()

    elif opcao == 4:
        break

