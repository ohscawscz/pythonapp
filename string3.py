

# sequence : 인덱싱과 슬라이싱에 대한 예제

str = 'Monty python'

print(str[0])

print(str[-1])

print(str[0:5])

print(str[:5])

print(str[6:])

date_weather = '202507225Sunny'

# 날짜(date)와 날씨(weather)을 출력하시오

date = date_weather[:8]
print(f'date : {date}')

weather = date_weather[-5:]
print(f'weather : {weather}')

# 날짜(date) 데이터를 2025년 07월 22일로 변환하여 출력하시오
# 2025년 07월 22일 날씨: Sunny

year = date[:4]
month =date[4:6]
day_of_month = date[6:]

print(f'{year}년 {month}월 {day_of_month}일 날씨 : {weather}')