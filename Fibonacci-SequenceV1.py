print('='*15)
print('Sequencia de Fibonacci')
print('='*15)
termo = int(input('Quantos Termos voce Quer ver: '))
conta = 3
n1 = 0
n2 = 1
print('{} - {}'.format(n1, n2), end=' ')
while conta <= termo:
    n3 = n1 + n2
    print(' {} -'.format(n3), end=' ')
    n1 = n2
    n2 = n3
    conta = conta + 1
print('FIM')
    