

"""
1. O programa escolhe um número aleatório entre 1 e 100.

2. O jogador tenta adivinhar o número inserindo valores no terminal.

3. Após cada tentativa, o programa fornece dicas baseadas na proximidade:

Muito perto: diferença de até 5.

Perto: diferença de até 10.

Um pouco longe: diferença de até 20.

Muito longe: diferença maior que 20.

4. O jogo termina quando o jogador adivinha o número, e o total de tentativas é exibido.

"""


import random 


def jogo_adivinhacao():
    print('Bem-vindo ao Jogo de Adivinhação!')
    
    # Escolhe nivel de dificuldade: 
    print('Escolha o nível de dificuldade: ')
    print('1. Fácil (1 a 50)')
    print('2. Médio (1 a 100)')
    print('3. Difícil (1 a 1000)')

   


    while True: 
        try: 
            dificuldade = int(input('Digite o número correspondente à dificuldade: '))

            if dificuldade == 1: 
                limite_superior = 50
                tentativas_max  = 10
                break
            elif dificuldade == 2: 
                limite_superior = 100
                tentativas_max = 10
                break
            elif dificuldade == 3: 
                limite_superior = 1000
                tentativas_max = 10
                break
            else: 
                print('Por favor, escolha uma opção válida (1, 2 ou 3).')

        except ValueError:
            print('Entrada inválida! Por favor, digite um número inteiro.')
    
    print(f'O computador escolheu um número entre 1 e {limite_superior}')
    print(f'Você tem {tentativas_max} tentativas para adivinhar o número.')


# Escolhe um número aleatorio dentro do limite definido pelo dificuldade

    numero_secreto = random.randint(1, limite_superior)
    tentativas = 0
    acertou = False


    while not acertou and tentativas < tentativas_max:
        try: 
            # Solicita o palpite do jogador
            palpite = int(input(f'Digite seu palpite (1 a {limite_superior}): '))
            if palpite < 1 or palpite > limite_superior:
                print(f'Por favor, escolha um número entre 1 e {limite_superior}.')
                continue

            tentativas += 1
            diferenca = abs(numero_secreto - palpite)

            # Verifica o palpite
            if palpite == numero_secreto:
                print(f'Parabéns! Você acertou o número em {tentativas} tentativas.')
                acertou = True
            elif diferenca <= 5:
                print('Muito perto! Tente novamente.')
            elif diferenca <= 10:
                print('Perto! Você está chegando lá.')
            elif diferenca <= 20:
                print('Um pouco longe! Continue tentando.')
            else:
                print('Muito longe! Tente outro número.')

            # Exibe o número de tentativas restantes
            print(f'Tentativas restantes: {tentativas_max - tentativas}')

        except ValueError:
            print('Entrada inválida! Por favor, digite um número inteiro.')

    if not acertou:
        print(f'Você perdeu! O número secreto era {numero_secreto}.')
               
        print('Obrigado por jogar!')

# Execute o jogo
if __name__ == '__main__':
    jogo_adivinhacao()
    
    
