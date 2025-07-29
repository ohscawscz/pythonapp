# '서시.txt' 파일에서 한 라인씩 읽어서 출력하는 예제 프로그램

file = None

try:
    # 1. file열기
    with open('서시.txt', 'r', encoding='utf-8') as file:
    # 2. file 읽기
        lines = file.readlines()
        num = 1
    for line in lines:
        print(f'{num} : {line.strip()}')
        num += 1

    print(lines)

except Exception as err:
    print(f'errr : {err}')
finally:
    if file is not None:
        # 3. 파일 리소스 해제
        file.close()