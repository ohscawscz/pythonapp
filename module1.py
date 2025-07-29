# 모듈에 대한 예제 프로그램

import random

colors  = ['red', 'yellow', 'green', 'blue']

print (random.choice(colors))

lotto_nums = random.sample(range(1, 46, 1), 6)

print(f'lotto_nums : {lotto_nums}')