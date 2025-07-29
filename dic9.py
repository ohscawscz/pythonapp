
dic = {'a': 1, 'b': 2, 'c': 3,}

print(dic.get('b'))
print(dic['b'])

print(dic.get('d', 'Not exist_key'))

print(dic['d'])  #KeyError