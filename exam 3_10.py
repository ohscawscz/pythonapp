number = input("계좌번호를 입력하세요")

temp = ''
for ch in number:
    if ch == '-':
        continue
    temp += ch

print(temp)