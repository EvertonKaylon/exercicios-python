lista = [[], []]
for c in range(1, 8):
	numero = int(input(f'Digite o {c}° Numero: '))
	if numero % 2 == 0:
		lista[0].append(numero)
	else:
		lista[1].append(numero)
print('–='*25)
lista[0].sort()
lista[1].sort()
print(f'Os Valores Pares Digitados Foram {lista[0]}')
print(f'Os Valores Ímpares Digitados Foram {lista[1]}')