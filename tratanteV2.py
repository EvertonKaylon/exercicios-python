ponto = 'S'
cont = soma = maior = menor = media = 0
while ponto in 'Ss':
    numero = int(input('Digite um numero: '))
    cont += 1
    total = soma + numero
    soma = total
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    ponto = str(input('Quer Continuar: [S/N] '))
media = soma / cont
print('voce digitou {} numeros e a media entre eles e {}'.format(cont, media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))
