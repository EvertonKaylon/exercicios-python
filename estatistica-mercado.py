maisDe1000 = 0
produtobarato = ' '
preçobarato = 0
total = 0
cont = 0
print('-'*25)
print('Lojas De Tudo um Pouco')
print('-'*25)
while True:
   produto = str(input('Nome Do Produto: '))
   preço = float(input('Preço: R$'))
   cont += 1
   continuar = ' '
   while continuar not in 'SN':
      continuar = str(input('Quer Continuar [S/N] ')).strip().upper()[0]
   if cont == 1 or preço < preçobarato:
      preçobarato = preço
      produtobarato = produto
   if total >= preço:
      total = preço + total
   else:
      total = preço + total 
   if preço > 1000:
      maisDe1000 += 1
   if continuar == 'N':
      break
print(f'A Total da Compra foi R${total:.2f}')
print(f'O Produto mais barato foi {produtobarato} que custa {preçobarato:.2f}')
print(f'Tem {maisDe1000} Produto(s) mais de 1000 reais!')