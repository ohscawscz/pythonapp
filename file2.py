# '서시.txt' 파일에서 한 라인씩 읽어서 출력하는 예제 프로그램

file = None

try:
    # 1. file열기
    file = open('서시.txt', 'r', encoding='utf-8')
    # 2. file 읽기
    lines = file.readlines()

    for line in lines:
        print(line.strip())

    print(lines)

except Exception as err:
    print(f'errr : {err}')
finally:
    if file is not None:
        file.close()