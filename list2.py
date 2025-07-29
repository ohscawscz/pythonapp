
_list = []

print(_list)
print(type(_list))
print(len(_list))

list1 = [1, 2, 3, 4, 5]
print(list1)

# print(dir(list1))
for i in list1:
    print(i, end = '\t')

print()
print( '='* 50)
list2 = list([1, 2, 3, 4, 5])

print(list2)
print(type(list2))

list3 = [1, '홍길동', 100, 100, 100]

for i in list3:
    print(i, end = '\t')