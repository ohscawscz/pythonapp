# 다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성 하시오.
# 아이디는 반드시 10자리 이상
# 패스워드는 반드시 8 ~ 16자리 사이
# 패스워드에 아이디가 포함되면 안됨
# 패스워드에는 다음의 특수 문자가 반드시 하나 이상 포함
#   (~, !, @, #, $, %, ^, &, *, _, ?)


def is_valid_signup(user_id, user_passwd):
    special_chars = "~!@#$%^&*_?"
    
    
    if len(user_id) < 10:
        return "아이디는 반드시 10자리 이사이어야 합니다"
    
    if len(user_passwd) < 8 or len(user_passwd) > 16:
        return "패스워드는 반드시 0 ~ 16자리 사이어야 합니다."
    
    if user_id in user_passwd:
        return("비밀번호에 아이디를 포함할 수 없습니다.")

    if not any(char in special_chars for char in user_passwd): #False
        return("비밀번호에 특수문자가 하나 이상 포함되어야 합니다.")

    return '회원가입에 성공하였습니다'



user_id = input('아이디를 입력해주세요 (10자리 이상): ')
user_passwd = input('비밀번호를 입력해주세요 (8~16자리 사이, 특수문자 포함:')

result = is_valid_signup(user_id, user_passwd)
print(result)