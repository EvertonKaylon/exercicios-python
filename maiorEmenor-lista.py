valores = []
maior =  menor = 0
for c in range(0,5):
	valores.append(int(input(f'Digite Um Número para a Posição {c}: ')))
	if c == 0:
		maior = menor = valores[c]
	else:
		if valores[c] > maior:
			maior = valores[c]
		if valores[c] < menor:
			menor = valores[c]

print(f'O Maior Número digitado Foi {maior} na posição', end=' ')
for c, v in enumerate(valores):
	if v == maior:
		print(f'{c}..', end=' ')
print()
print(f'O Menor Número digitado Foi {menor} na posição', end=' ')
for c, v in enumerate(valores):
	if v == menor:
		print(f'{c}..', end=' ')
print()