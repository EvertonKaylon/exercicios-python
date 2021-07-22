numero = soma = conta = 0
while True:
    numero = int(input('Digite um Numero: (999 para PARAR) '))
    if numero == 999:
        break
    soma += numero
    conta += 1
print(f'A Soma dos {conta} Numeros e {soma}')