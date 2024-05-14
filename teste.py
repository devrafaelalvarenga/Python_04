base_calculo_media = 4
dict_aluno = dict()
nome = False
nota = False

while nome is not True:
    try:
        dict_aluno['nome'] = str(input('Informe seu nome: ')).title()
        if len(dict_aluno['nome']) == 0:
            print('Digite um nome valido')
        elif any(char.isdigit() for char in dict_aluno['nome']):
            print('Digite um nome valido. Não pode conter numeros') 
        else:
            nome = True
    except ValueError as e:
        print(e)
        exit()

while nota is not True:
    dict_aluno['nota_b1'] = float(input('informe sua nota no primeiro bimestre: '))
    dict_aluno['nota_b2'] = float(input('informe sua nota no segundo bimestre: '))
    dict_aluno['nota_b3'] = float(input('informe sua nota no terceiro bimestre: '))
    dict_aluno['nota_b4'] = float(input('informe sua nota no quarto bimestre: '))
    try:
        if dict_aluno['nota_b1'] < 0 or dict_aluno['nota_b1'] > 10:
            print('Informe uma nota valida')
        elif dict_aluno['nota_b2'] < 0 or dict_aluno['nota_b2'] > 10:
            print('Informe uma nota valida')
        elif dict_aluno['nota_b3'] < 0 or dict_aluno['nota_b3'] > 10:
            print('Informe uma nota valida')        
        elif dict_aluno['nota_b4'] < 0 or dict_aluno['nota_b4'] > 10:
            print('Informe uma nota valida')
        else:
            nota = True   
    except ValueError as e:
        print(e)
        exit()        

media = (dict_aluno['nota_b1'] + dict_aluno['nota_b2'] + dict_aluno['nota_b3'] + dict_aluno['nota_b4']) / base_calculo_media

if media >= 7:
    dict_aluno['situacao'] = 'aprovado'
elif media < 7:
    dict_aluno['situacao'] = 'reprovado'


print(f'Nome do aluno: {dict_aluno['nome']}')        
print('Média do aluno:',media)
print('Situação:',dict_aluno['situacao'])
