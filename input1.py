# 정수를 키보드로 입력 받아서 사칙 연산을 출력하는 프로그램을 구현하시오 (+, -, *, /)

a= int(input('정수를 입력해주세요 '))
b= int(input('정수를 입력해주세요 '))

sum = a+b
print(sum)

subtraction = a-b
print(subtraction)

multiply = a*b
print(multiply)

divide = a/b
print(divide)

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')