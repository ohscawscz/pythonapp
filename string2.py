# 키보드를 사용하여 정수를 입력 받아서 출력하는 프로그램

score = int(input('정수를 입력해주세요 '))

print(f'score : {score}')
print(f'score 자료형: {type(score)}') # str

line = '=' * 100

print(line)

a = 14.5

print(int(a)) 

num_str = '1234.567'

print(float(num_str))

print(f'num_str : {float(num_str): .2f}')

b = 'python'

# print(int{num_str}) # ValueError