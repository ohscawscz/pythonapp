

colors = ['yellow', 'green', 'blue', 'yellow']

print(colors.index('yellow')) # index

print(colors.index('yellow', 1)) 

print(colors.index('yellow')) # index

# print(colors.index('red')) # ValueError

num_list = [1, 3, 2]

num_list.reverse()

print(num_list)

# 오름차순 정렬
num_list.sort()

print(num_list)

# 내림차순 정렬
num_list.sort(reverse=True)

print(num_list)