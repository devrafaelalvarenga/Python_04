# criar dicionario
nome = dict()

# adicionar ou substituir dados
nome['nome'] = 'rafael'
nome['ano_nascimento'] = 1988
nome['sexo'] = 'm'
#nome['teste'] = 'teste'
#print(nome)
'''
# excluind info
del nome['teste']
print(nome)

print(nome.values())
print(nome.keys())
print(nome.items())
print(f'{nome["nome"]}' nasceu em {nome["ano_nascimento"]})

for k, v in nome.items():
    print(f"{k} é {v}")


cadastro = list()

nome2 = {'nome':'mayara', 'ano_nascimento':1989, 'sexo':'f'}
cadastro.append(nome)
cadastro.append(nome2)

print(cadastro)
print(cadastro[0])
print(cadastro[1]['nome'])
'''

estado = dict()
brasil = list()

for d in range(0,2):
    estado['uf'] = str(input('Informe a unidade federativa do estado: '))
    estado['sigla'] = str(input('Informe a sigla do estado: '))
    #utilizado .copy para nao duplicar os dados pois sem o sufixo os valores iniciais sao sobrepostos
    brasil.append(estado.copy())
#print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()