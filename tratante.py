numero = int(input('Digite um numero: [999 para Parar] '))
cont = lixo = soma = 0
add = numero
while numero != 999:
    numero = int(input('Digite um numero: [999 para Parar] '))
    cont = cont + 1
    if numero == 999:
        lixo = numero
    else:
        result = add + soma
        soma = result
print('voce digitou {} numeros e a soma deles e {}'.format(cont, result))
