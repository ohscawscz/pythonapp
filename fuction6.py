
# 정수를 입력 받아서 짝수인 경우 True, 홀수인 경우는 False를 변환하는 함수를 정의

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

# for i in range(1, 101, 1):
#     if is_even(i):
#         print(i)


while True:
    answer = input('짝수읹지 확인할 숫자를 입력하세요 (종료 : q)')
    if answer == 'q':
        break
    num = int(answer)
    if is_even(num):
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 짝수가 아닙니다.')

