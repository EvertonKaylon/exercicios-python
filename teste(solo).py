lista = []
lista2 = [2, 7, 9, 1]
while True:
	num = int(input('Digite um Número: '))
	if num % 2 == 0:
		lista.append(num)
	else:
		conc = lista + lista2
		lista.append(conc)
	pergunta = str(input('Quer Continuar? [S/N] '))
	while pergunta not in 'sSnN':
		pergunta = str(input('Quer Continuar? [S/N] '))
	if pergunta in 'nN':
		break

if len(lista) > 5:
	print(lista)
	print(lista[3])
else:
	print(lista)