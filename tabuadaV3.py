while True:
    pergunta = int(input('Digite um Numero para ver sua Tabuada: '))
    if pergunta == 0:
        break
    for c in range(1,11):
        soma = pergunta * c
        print(f'{pergunta} x {c} = {soma}')
print('PRROGRAMA FINALIZADO! Volte Sempre.')