
# 사용자로부터 두 수를 입력 받아 둘 중에서 큰 수를 출력하는 프로그램입니다.
# 조건 연산자 사용할 것

num_1 = int(input("첫 번째 정수 : "))
num_2 = int(input("두 번째 정수 : "))

max_value = (num_1 if num_1 > num_2 else num_2)

print(f'{num_1}과 {num_2} 중 큰 수는 {max_value}')