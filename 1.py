# Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', e caso exista,
# salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.
def find_value(search_value, item):
    if search_value in item:
        return True
    else:
        return False

#fill dictionary list with user input
dic_list = []
n = int(input('Type list range:\n'))
d = int(input('Type dictionary range:\n'))

for p in range(n):
    dic_list.append( dict(input().split() for i in range(d)) )

#check if key given by user exists in the dictionary list
# r = int(input('Type search range:\n'))
# for i in range(r):
search_key = input('By what key you want to search ?\n')
key_list = [] #list of keys that were found in the list
for dic in dic_list:
    if find_value(search_key, dic) and not(find_value(search_key, key_list)):
        # print(search_key)
        key_list.append(search_key)
    else:
        pass
print('dictionary list: ', dic_list)
print('keys list: ', key_list)
