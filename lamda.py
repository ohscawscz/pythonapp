

# 람다 함수에 대한 예제 프로그램

# def hello(user_name):
    # return "Hello," + user_name

hello = lambda user_name: 'Hello,' + user_name

print(type(hello)) # function 객체

print(hello(('hjk')))
