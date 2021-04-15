import random

def main():

    print("""
    Bem vindo ao jogo de adivinhação do número.
    Tente adivinhar no menor número de tentativas possiveis, o número secreto.
    """)

    secretNumber = random.randrange(1, 10)
    playerNumber = 0

    while playerNumber != secretNumber:
        
        playerNumber = int(input('Entre 1 e 10, qual o seu palpite para o número secreto?: '))

        if  playerNumber > secretNumber:
            print(f'O número {playerNumber} é maior que o número secreto.')

        elif playerNumber < secretNumber:
            print(f'O número {playerNumber} é menor que o número secreto.')
    
    print('Você acertou o número secreto! Parabéns.')
    
    return print('Fim do jogo.')

main()