
# 키워드 기반 가변 인수 함수에 대한 예제

def print_info(**kargs):
    print(f'kwargs : {kargs}')
    print(f'kwargs 자료형 : {type(kargs)}')

    for key, value in kargs.items():
        print(f'{key} : {value}')
# 함수 호출
print_info(username='아이유', age=10) 

print_info(username='아이유', age=10, gender='여') 