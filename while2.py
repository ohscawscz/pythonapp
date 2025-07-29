
str = 'yes'
num = 0
while str == 'yes' :
    total = int(input('숫자를 입력하세요 : '))
    num += total
    str = input('계속 (yes/no) ? ')
print(f'입력한 숫자들의 합 : {num}')


  