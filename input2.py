# 정수를 키보드로 입력 받아서 사칙 연산을 출력하는 프로그램을 구현하시오 (+, -, *, /)

a, b = list(map(int, input("두 개의 정수를 입력하세요(공백) : ").split())) # [1, 5] : unpacking

print(f'a : {a}, b : {b}')

print(type(a))
print(type(b))

print('=' * 100)

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')