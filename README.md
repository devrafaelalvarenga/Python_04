# python_04

## typehint é uma dica de tipagem 'Boa pratica'. Ele nao valida/altera nenhuma variavel 

idade = 25 #inteiro
idade: int = 25

nome = 'ana' #string
nome: str = 'ana'

lista = []
dicionari = {chave:valor}

ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True)

A função sorted() retorna uma lista classificada do objeto iterável especificado.
#sorted(iterable, key=key, reverse=reverse)

key=itemgetter()
#coletor de itens #

reverse=True
#ordenação dos itens
