
num = int(input('합을 계산할 숫자를 입력하세요 : '))

total = 0
for i in range(1, num+1, 1):
    total += i
print(f'1부터 10까지의 합은 : {total}')