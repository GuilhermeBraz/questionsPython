import csv
import operator
# Retorne uma lista com os registro ordenados por nome. Exemplo de arquivo:
# Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade.

#open and read csv file, spliting it by ;
csv_file = open('test.csv', 'r')
csv1 = csv.reader(csv_file, delimiter=';')

header = next(csv1, None) #skip header
#sort by name
sort = sorted(csv1, key = operator.itemgetter(1))   #name is in index 1


sort.insert(0, header)  #add header to list
#print sorted list
print(sort)
