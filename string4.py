#문자열의 길이를 구하는 예제

str = input('문자열을 입력하세요 : ').strip()

if len(str) == 0:
    print('문자열을 정확히 입력하세요')
    exit(0)

if len(str) % 2 == 0:
    mid = len(str) // 2
    print(str[mid - 1 : mid + 1])
else: 
    mid = (len(str)) // 2
    print(str[mid])