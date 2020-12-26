#Function to search for value in list
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
search_key = input('By what key you want to search ?\n')
key_list = []   #list of keys that were found in the list

#loop to append the value you want to search on the list of found keys
for dic in dic_list:
    if find_value(search_key, dic) and not(find_value(search_key, key_list)):
        # print(search_key)
        key_list.append(search_key)
    else:
        pass
print('dictionary list: ', dic_list)
print('keys list: ', key_list)
