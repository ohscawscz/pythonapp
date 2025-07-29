
#리스트 함수에 대한 예제

lst = [1, 2, 3]

lst.append(4)

print(lst)

lst.extend([5, 6])

print(lst)

lst.insert(1, 'b')

print(lst)

lst.pop()
print(lst)


if 'b' in lst:
    lst.remove('b')

print(lst)

lst.clear()
print(lst)