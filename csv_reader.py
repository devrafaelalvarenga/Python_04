import csv

path: str = 'exemplo.csv'

file_csv: list = list()

with open (file=path, mode='r', encoding='utf-8') as file:
    #lendo arquivo csv transformando em dicionario
    reader_csv = csv.DictReader(file)
    #reader_csv = csv.reader()

    for r in reader_csv:
        file_csv.append(r)

print(file_csv)        

