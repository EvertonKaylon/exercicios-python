exp = str(input('Digite Sua Expressão: '))
pilha = []
for simbol in exp:
	if simbol ==  '(':
		pilha.append('(')
	elif simbol == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print('A Expressão está válida!')
else:
	print('A Expressão está inválida!')