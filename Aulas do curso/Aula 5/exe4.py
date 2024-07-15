pombinhos = {'Noivo':'Josué',
             'Noiva':'Leandra',
             'Amantes do Noivo': ['Bruno','Guilherme','Jeff']}

pombinhos['Amantes do Noivo'].remove('Guilherme')

for chave, valor in pombinhos.items():
    print(f'{chave} : {valor}')

pombinhos.pop('Amantes do Noivo')

for chave, valor in pombinhos.items():
    print(f'{chave} : {valor}')
