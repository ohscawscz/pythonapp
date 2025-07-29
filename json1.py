
# member 라는 dictinary 객체를 member json
import json


# dictinary

member = {
    'user_id' : 'python',
    'user_name' : '일길동',
    'age' : 10,
    'email' : 'python@gmail.com',
}

print(type(member))
print(member)

try:
    with open('member.json', 'w', encoding='utf-8') as file:
        json.dump(member, file, ensure_ascii= False)

except Exception as err:
    print(f'err : {err}')