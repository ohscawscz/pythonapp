

_set = { 1, 3, 2, 5, 2}
print(_set)
print(type(_set))

for i in _set:
    print(i)

print(dir(_set))

#추가
_set.add(10)
print(_set)

#삭제
_set.remove(2)
print(_set)