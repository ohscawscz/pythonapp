
menu = {
    '칼국수': 6000,
    '비빔밥': 5500,
    '돼지국밥': 7000,
    '돈까스': 7000,
    '김밥': 2000, 
    '라면': 2500,
}

menu['냉면'] = 1000
for key, value in menu.items():
    if value < 6000:
        print(f'메뉴 {key} : {value}원')

# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 수 있도록 하시오.(동이랗ㄴ 메뉴는 가격만 변경)

new_menu, new_price = input('추가할 메뉴를 입력해 주세요 (동일한 메뉴는 가격만 변경): ').split()

menu.update({new_menu: new_price})

# is_updated = False
# for name in menu.keys():
#     if name == new_menu:
#         menu[name] = new_price
#         is_updated = True
# if not is_updated:
#     menu[new_menu] = new_price

print(menu)
