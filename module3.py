# import math

# print(f'원주율 : {math.pi}')

# print(f'지수 함수 : {math.exp(2)}')

# from math import pi, exp
# print(f'원주율 : {pi}')

# print(f'지수 함수 : {exp(2)}')
import mymodule

from mymodule import calculate_circle_area, MAX_VALUE, radius # myboudle.py 에서 들고온 모듈

print(calculate_circle_area(5))

result = mymodule.calculate_circle_area(5)
print(f'원의 넓이 : {result:.2f}')

print(f'MAX_VALUE : {MAX_VALUE}')

print(f'radius : {radius}')


