
score = int(input('성적을 입력해주세요'))

if score >= 90:
    print('A')
elif score >= 80: # score < 90 and score >= 80 (80 <= score < 90) 
    print('B')
elif score >= 70: # score < 80 and score >= 70 (70 <= score < 80)
    print('C')
elif score >= 60: # score < 70 and score >= 60 (60 <= score < 70)
    print('D')
else: # score < 60
    print('F')