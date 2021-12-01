lista = []
for n in range(0, 5):
	num = int(input('Digite Um Número: '))
	if n == 0 or num > lista[-1]:
		lista.append(num)
		print('adicionado na última posição...')
	else:
		pos = 0
		while pos < len(lista):
			if num <= lista[pos]:
				lista.insert(pos, num)
				print(f'adicionado na posição {pos}...')
				break
			pos += 1
print(f'A Lista Ordenada ficou: {lista}')