#faça um programa que leia e a media de um aluno, 
#guardando tambem a situaçao em um dicionario
#no final mostre o conteudo da estrutura na tela

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

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter #coletor de itens #

ranking = dict()

ranking['jogador_1'] = randint(1, 6)
ranking['jogador_2'] = randint(1, 6)
ranking['jogador_3'] = randint(1, 6)
ranking['jogador_4'] = randint(1, 6)

ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True)
print('=== Ranking de jogadores ===')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(1)