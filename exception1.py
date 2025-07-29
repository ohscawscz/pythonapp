
# exception handling에 대한 예제

try:
    num = int(input('하나의 숫자를 입력해주세요'))
    print(f'num : {num}')
except ValueError as err:
    print(f'err : {err}')
print('end!!')