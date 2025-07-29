
# 언패킹에 대한 예제 프로그램

# 함수 정의

def print_all(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')

_list = [1, 2, 3]

print_all(*_list)

# print_all(_list)