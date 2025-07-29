

# 두 수의 합을 구하는 함수
# 세 숫자의 수의 합을 구하는 함수
# 네 숫자의 수의 합을 구하는 함수

def add_many(*args):
    # print(f'args ; {type(args)}')
    # print(f'args ; {args}')
    total = 0
    for i in args:
        total += i
    return total


print (add_many(1, 2))
print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4))