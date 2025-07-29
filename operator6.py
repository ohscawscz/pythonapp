
# 논리 연산자에 대한 예제 프로그램입니다.
# 이런 코드는 파이썬만 지원 다른 언어에서는 지원 안됨

score = 90

# result = 0 <= score <= 100

result = score >= 0 and score <= 100 # 이 코드가 다른 언어에서 쓰는 논리 연산자

print(result)

result = score >= 0 and score <= 100

print(result)   

result = score < 0 or score > 100

print(result)

flag = True

result = not flag

print(result) # False