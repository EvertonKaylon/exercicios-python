lista = []
pares = []
impares = []
while True:
	num = int(input('Digite um Número: '))
	if num % 2 == 0:
		lista.append(num)
		pares.append(num)
	else:
		lista.append(num)
		impares.append(num)
	pergunta = str(input('Quer Continuar? [S/N]: '))
	if pergunta in 'nN':
		break
lista.sort()
print(f'A Lista Completa {lista}')
pares.sort()
print(f'A Lista com Números Pares: {pares}')
impares.sort()
print(f'A Lista com Números Ímpares: {impares}')