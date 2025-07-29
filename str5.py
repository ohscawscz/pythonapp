

str = 'string indexing'

print(str)
print(type(str))
print(dir(str))   # __iter__ : iterable : 반복가능한 객체


#indexing
print(str[0])
print(str[-1])

# sliicing
print(str[0:6])
print(str[-8:-3])

# for - in 문을 사용하여 문자 출력
for ch in str:
    print(ch)


result = 'i' in str
print(f'result " {result}')

