termo = int(input('termo: '))
razao = int(input('razao: '))
decimo = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -'.format(decimo), end=' ')
        decimo = decimo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos Termos Voce Quer mostrar a Mais: '))
print('Programa Finalizado Com {} Termos Mostrados'.format(total))
