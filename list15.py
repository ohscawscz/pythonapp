
import random
# 4. 메뉴를 랜덤으로 선택하여 ㅜㄹ력하는 코드 

menu = [['칼국수', 6000], ['비빔밥', 5500], ['돼지국밥', 7000],
         ['돈가스', 7000], ['김밥', 2000],['라면', 2500],]

result = random.choice(menu)
print(result)