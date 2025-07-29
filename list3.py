
#list에 대한 예제
# 인덱싱과 슬라이싱

colors = ['red', 'green', 'blue', 'pink', 'purple']

# index 조회
for i in range(len(colors)):
    print(f'index : {i}')


# red, blue 를 인덱스를 사용하여 조회하시오
print(colors[0])
print(colors[2])
print(colors[-1])

lst = [1, 2, 3]
print(lst)

lst [-3] = 'b'
print(lst)

lst[-1] = lst[1] *2
print(lst)

lst[-2] = lst[0] * lst[2]
print(lst)