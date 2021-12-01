lista = []
while True:
	lista.append(int(input('Digite um Número: ')))
	perg = str(input('Quer Continuar? [S/N]: '))
	if perg in 'nN':
		break
if 5 in lista:
	print('O Número 5 está na lista!')
else:
	print('O Número 5 Não está na Lista')
print(f'A Lista tem {len(lista)} Elementos' )
lista.sort(reverse=True)
print(f'A Lista em Ordem Decrescente: {lista}')