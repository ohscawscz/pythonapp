# 실습문제 2

# first = 'python is'

# inputt = input("입력해 : ")

# print(first + inputt)


# a = int(input("사각형의 가로의 길이 : "))
# b = int(input("사각형의 세로의 길이 : "))

# print(a * b)

# a = float(input("사각형의 가로의 길이 : "))
# b = float(input("사각형의 세로의 길이 : "))

# area = a * b
# print(f'사각형의 넓이 : {area:.2f}')


a = int(input("초단위의 시간을 입력하세요 : "))

min = a // 60
sec = a % 60

print(f'{a}초는 {min}분 {sec}초 입니다.')