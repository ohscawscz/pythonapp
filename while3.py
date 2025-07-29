

total = 0
count = 0
is_contunue = True
while is_contunue:
    score = int(input('성적을 입력하세요 :'))
    if score >=0:
        total += score
        count += 1
    else:
        is_contunue = False
avg = total / count

print(f'합계 : {total} 평균 : {avg:2f}')