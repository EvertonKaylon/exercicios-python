grupo = []
dado = []
maior = menor = 0
Pergunta = 'Ss'
while True:
	dado.append(str(input('Nome: ')))
	dado.append(float(input('Peso: ')))
	if len(grupo) == 0:
		maior = menor = dado[1]
	else:
		if dado[1] > maior:
			maior = dado[1]
		if dado[1] < menor:
			menor = dado[1]
	grupo.append(dado[:])
	dado.clear()
	Pergunta = str(input('Quer Continuar? [S/N] '))
	while Pergunta not in 'SsNn':
		Pergunta = str(input('Quer Continuar? [S/N] '))
	if Pergunta in 'Nn':
			break
print('_'*50)
print(f'Ao Todo Foram Cadastradas {len(grupo)} Pessoas')
print(f'O Maior Peso Foi de {maior}Kg, Peso de ', end='')
for p in grupo:
	if p[1] == maior:
		print(f'{p[0]} ', end=' ')
print()
print(f'O Menor Peso Foi de {menor}Kg, Peso de ', end='')
for p in grupo:
	if p[1] == menor:
		print(f'{p[0]} ', end=' ')
print()
	