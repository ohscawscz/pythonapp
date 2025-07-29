
# 디폴트인수
# 함수 정의
def greet(name, msg = 'good moring'):
    print(f'{msg}, {name}')

greet('철수', '좋은 아침')
greet('철수')