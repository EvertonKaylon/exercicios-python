from random import randint
print('x-'*20)
print('  Jogo Do Par ou Impar  ')
print('x-'*20)

v = 0
while True:
    escolha = str(input('Tu Escolhe Par ou Impar: [P/I] ')).strip().upper()[0]
    jogador = int(input('Digite um Numero de 0 a 10: '))
    computador = randint(0,10)
    soma = jogador + computador
    print(f'O Jogador jogou {jogador} e o Computador jogou {computador}, Deu {soma}')
    while escolha not in 'PI':
        escolha = str(input('Tu Escolhe Par ou Impar: [P/I] ')).strip().upper()[0]
    if escolha == 'P':
        if jogador % 2 == 0:
            print('Voce VENCEU!')
            v += 1
            print('Vamos Novamente...')
        else:
            print('Voce PERDEU!')
            break
    if escolha == 'I':
        if jogador % 2 == 1:
            print('Voce VENCEU!')
            v += 1
            print('Vamos Novamente...')
        else:
            print('Voce PERDEU!')
            break
print(f'GAME OVER! Voce venceu {v} vezes')
