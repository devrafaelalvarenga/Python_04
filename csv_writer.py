import csv

file_name = 'exemplo_2.csv'

row = ['yasmin', 14, 16.03, True]

rows = [['doki', 6, 14.12, True], 
       ['donna', 2, 12.06, True]]

with open(file=file_name, mode='w', encoding='utf-8') as file:
    #escrevendo no arquivo
    csv_writer = csv.writer(file)
    #uma linha
    csv_writer.writerow(row)
    #varias linhas
    csv_writer.writerows(rows)

