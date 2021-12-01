lista = []
while True:
	num = int(input('Digite um Número: '))
	if num not in lista:
		lista.append(num)
		print('Valor Adicionado com Sucesso!')
	else:
		print('Valor Duplicado não Adicionado')
	pergunta = str(input('Quer Continuar? [S/N]: '))
	if pergunta in 'nN':
		break
lista.sort()
print(lista)