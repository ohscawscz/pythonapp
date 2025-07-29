import string
import random

# def genPass():
#     for i in range(3):
#         pw = random.choice(["q2sdas", "q34grw", "z14erw"])
#         print(pw)

# genPass()



def genpass():
    str = string. ascii_lowercase + string.digits
    password = ''

    for _ in range(6):  # 변수를 사용하지 않겠다는 의미
        password += random.choice(str)
    
    return password

print(genpass())
print(genpass())
print(genpass())