
price = int(input('물건을 구입한 금액은 얼마입니까? '))
if price > 100000:
    discount = int(price * 0.05)
else:
    discount = 0
final_price = price + discount

print(f'물건 구입시 할인금액 : {discount} 원')
print(f'최종 지불금액 : {final_price} 원')