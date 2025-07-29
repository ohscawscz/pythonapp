
# 위치 인수 (positional augument). 키워드(keyword) 인수

def calc(x, y, z):
    print(f'x = {x}, y = {y}, z = {z}')

calc(1, 2, 3) # positional augument
calc(y= 2,z=3, x=1) # keyword augument

calc(1, z=3, y=2)