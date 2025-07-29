
# 2장 1번 실습 문제

# num_1 = int(input('첫 번째 정수 : '))
# num_2 = int(input('두 번째 정수 : '))

# # if num_1 > num_2:
# #     print(f'{num_1}과 {num_2} 중 큰 수는 {num_1}')
# # else:
# #     print(f'{num_1}과 {num_2} 중 큰 수는 {num_2}')
    
# max_value = (num_1 if num_1 > num_2 else num_2) # 이 방법 추천


# 2장 2번 실습 문제
# kg = int(input('짐의 무게는 얼마입니까? : '))

# if kg >= 20:
#     print('짐에 대한 요금은 20000원입니다.')
# else:
#     print('짐에 대한 수수료는 없습니다.')
# print('감사합니다')

# 2장 3번 실습 문제
# price = int(input('물건을 구입한 금액은 얼마입니까? : '))

# if price >= 100000:
#     sale = int(price * 0.05)
# else:
#     print(sale = 0)
# total = price - sale
# print(f'물건 구입시 할인금액 : {sale}')
# print(f'최종 지불금액 : {total}원')

# 2장 4번 실습 문제
# str = input('문자열을 입력하세요 : ')

# length = len(str)

# if length % 2 == 1:
#     mid = length // 2
#     print(f'가운데 문자 : {str[mid]}')
# else:
#     mid1 = (length // 2) -1
#     mid2 = length // 2
#     print(f'가운데 문자 : {str[mid1]} {str[mid2]}')


# 2장 5번 실습 문제
# time = int(input('근무시간을 입력하세요 : '))
# time_money = int(input('시간당 임금을 입력하세요 : '))

# if time > 40:
#     money = 40 * time_money
#     nice = (time - 40) * time_money * 1.5
#     total_pay = int(money + nice)
# else:
#     total_pay = int(time * time_money)
# print(f'총 임금은 {total_pay}원 입니다')
    


# 2장 6번 실습 문제입니다.

# kg = int(input('짐의 무게는 얼마입니까? : '))

# if kg <= 20:
#     print('짐에 대한 요금은 무료 입니다.')
# elif kg <= 30:
#     over = kg - 20
#     total = int(over * 1000)
#     print(f'짐에 대한 요금은 {total}원 입니다\n감사합니다')
# elif kg > 30:
#     print('짐을 부칠 수 없습니다.\n감사합니다')


# 2장 8번 실습 문제

# def menu():
#     print('1: 삼각형    2: 사각형   3:원    4:종료')
#     selection = int(input('면적을 계산할 도형을 선택하세요 : '))
#     return selection

# def tri(a, b):
#     return (a * b) // 2

# def input_tri():
#     t = int(input('밑변 : '))
#     h = int(input('높이 : '))
#     return t, h

# def spah(a, b):
#     temp = a * b
#     return temp

# def input_spah():
#     t = int(input('가로 : '))
#     h = int(input('세로 : '))
#     return t, h

# def circle(radius):
#     temp = 3.14 * radius ** 2
#     return temp

# def input_cir():
#     r = int(input('원의 반지름을 적어 : '))
#     return r
# def main():
#     while True:
#         index = menu()

#         if index == 1:
#             t, h = input_tri()  # 두 값 한 번에 받기
#             result = tri(t, h)
#             print(f'삼각형의 면적: {result}')
#         elif index == 2:
#             t, h = input_spah()
#             result = spah(t, h)
#             print(f'사각형의 면적 : {result}')
        
#         elif index == 3:
#             r = input_cir()
#             result = circle(r)
#             print(f'원의 지름 : {result}')

#         else:
#             break
# main()
