idade = mais18 = homem = mulher20 = 0
escolha = 'S'
while True:
    print('-'*20)
    print('Cadastre Uma Pessoa')
    print('-'*20)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: ')).strip().upper()[0]
    print('_'*20)
    escolha = ' '
    while escolha not in 'SN':
        print('Por Favor, Digite Somente (S)im Ou (N)ao!')
        escolha = str(input('Quer Continuar: ')).strip().upper()[0]
    if escolha == 'N':
        break
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
print(f'Pessoas com Mais de 18 anos: {mais18}')
print(f'Homens Registrados: {homem}')
print(f'Mulheres com Menos de 20 anos: {mulher20}')
