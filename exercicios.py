#faça um programa que leia e a media de um aluno, 
#guardando tambem a situaçao em um dicionario
#no final mostre o conteudo da estrutura na tela

base_calculo_media = 4
dados_do_aluno = dict()
aluno = list()
resultado: str

dados_do_aluno['nome'] = str(input('Informe seu nome: '))
dados_do_aluno['nota_b1'] = float(input('informe sua nota: '))
dados_do_aluno['nota_b2'] = float(input('informe sua nota: '))
dados_do_aluno['nota_b3'] = float(input('informe sua nota: '))
dados_do_aluno['nota_b4'] = float(input('informe sua nota: '))
aluno.append(dados_do_aluno.copy())

for d in aluno:
    media = (d['nota_b1'] + d['nota_b2'] + d['nota_b3'] + d['nota_b4']) / base_calculo_media

    if media >= 7:
        resultado = 'aprovado'
    elif media < 7:
        resultado = 'reprovado'

print(f'Nome do aluno: {d['nome'].title()}')        
print('Média do aluno:',media)
print('Situação é igual a',resultado)

# REFATORANDO

base_calculo_media = 4
dados_do_aluno = dict()
aluno = list()
resultado: str
nome = False
nota = False

while nome is not True:
    try:
        dados_do_aluno['nome'] = str(input('Informe seu nome: '))
        if len(dados_do_aluno['nome']) == 0:
            print('Digite um nome valido')
        elif any(char.isdigit() for char in dados_do_aluno['nome']):
            print('Digite um nome valido. Não pode conter numeros') 
        else:
            nome = True
    except ValueError as e:
        print(e)
        exit()

while nota is not True:
    dados_do_aluno['nota_b1'] = float(input('informe sua nota no primeiro bimestre: '))
    dados_do_aluno['nota_b2'] = float(input('informe sua nota no segundo bimestre: '))
    dados_do_aluno['nota_b3'] = float(input('informe sua nota no terceiro bimestre: '))
    dados_do_aluno['nota_b4'] = float(input('informe sua nota no quarto bimestre: '))
    try:
        if dados_do_aluno['nota_b1'] < 0 or dados_do_aluno['nota_b1'] > 10:
            print('Informe uma nota valida')
        elif dados_do_aluno['nota_b2'] < 0 or dados_do_aluno['nota_b1'] > 10:
            print('Informe uma nota valida')
        elif dados_do_aluno['nota_b3'] < 0 or dados_do_aluno['nota_b1'] > 10:
            print('Informe uma nota valida')        
        elif dados_do_aluno['nota_b4'] < 0 or dados_do_aluno['nota_b1'] > 10:
            print('Informe uma nota valida')
        else:
            aluno.append(dados_do_aluno.copy())   
            nota = True   
    except ValueError as e:
        print(e)
        exit()        

for d in aluno:
    media = (d['nota_b1'] + d['nota_b2'] + d['nota_b3'] + d['nota_b4']) / base_calculo_media

    if media >= 7:
        resultado = 'aprovado'
    elif media < 7:
        resultado = 'reprovado'

print(f'Nome do aluno: {d['nome'].title()}')        
print('Média do aluno:',media)
print('Situação é igual a',resultado)