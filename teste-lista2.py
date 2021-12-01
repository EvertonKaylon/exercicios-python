valores = []
for cont in range(0, 5):
	valores.append(int(input('Digite Um Número: ')))

for c, v in enumerate(valores):
	print(f'Na Posição {c}, Encontrei o  Número {v}')
print('Cheguei no Fim da Lista')