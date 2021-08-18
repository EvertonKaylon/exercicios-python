num = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete',
    'Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze',
    'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    perg = int(input('Digite Um Número de 0 á 20: '))
    if 0 <= perg <= 20:
        break
    else:
        print('Tente Novamente.', end=' ')
print(f'Você Digitou O Número {num[perg]}')
    