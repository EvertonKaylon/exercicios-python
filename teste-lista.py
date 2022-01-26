num = [1,2,4,5,6]
num[2] = 7
num.sort()
num.pop(3)
num.insert(2, 2)
if 5 in num:
	num.remove(2)
else:
	print('Não Achei o Número 5')
print(num)
print(f'Está Lista tem {len(num)} Elementos')
#print('A Lista em Ordem Decrescente: {}').format(num.sort(reverse=True))