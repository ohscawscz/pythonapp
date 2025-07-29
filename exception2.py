
# 함수 정의
def divide(a, b):

    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다.')
    return a / b


# 함수 호출
try:
    result = divide(10, 5)
    print(f'result : {result}')
except ZeroDivisionError as err:
    print(f'err : {err}')

print('end')