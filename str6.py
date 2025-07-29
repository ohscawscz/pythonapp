
str = 'ptyhon string'

idx = str.find('string')

print(f'index : {idx}')

print(f'str 문자열의 길이 {len(str)}')

print(f't 문자의 개수 : {str.count("t")}')

print(f'str 대문자로 변환 : {str.upper()}')

print(f'str : {str}')

str = '   python string    '

str2 = str.strip()

print(f'str2 : {str2}')
print(f'str2 문자열의 길이  : {len(str2)}')
print(f'str2 문자열의 길이  : {len(str)}')

str3 = 'python string'

str4 = str3.replace('string', '문자열')
print(f'str4 : {str4}')
