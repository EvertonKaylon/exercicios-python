times = ('PALMEIRAS','ATLETICO-MG','FORTALEZA','BRAGANTINO', 'ATHLETICO-PR','FLAMENGO', 
'BAHIA','FLUMINENSE','SANTOS','ATLÉTICO-GO','CORINTHIANS','INTERNACIONAL','CEARA SC',
'JUVENTUDE','CUIABA','SÃO PAULO','SPORT RECIFE','AMERICA-MG','GREMIO','CHAPECOENSE')

print(f'Lista de Time do Brasileirão: {times}')
print('=0' * 10)
print(f'Os Cinco Primeiros Colocados: {times[0:5]}')
print('=0' * 10)
print(f'Os Ùltimos Colocados: {times[16:]}')
print('=0' * 10)
print(sorted(times))
print(f'A Chapeoense está na {times.index("CHAPECOENSE")+1}ª Colocação!')
