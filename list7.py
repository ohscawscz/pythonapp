
student_scores = [[1, '일길동', 100, 100, 100],
                  [2, '이길동', 90, 90, 90],
                  [3, '삼길동', 80, 80, 80]]

print(student_scores[0])
print(type(student_scores[0]))

print(f'번호 : {student_scores[0][0]}')
print(f'이름 : {student_scores[0][1]}')
print(f'국어 : {student_scores[0][2]}')
print(f'영어 : {student_scores[0][3]}')
print(f'수학 : {student_scores[0][4]}')

print(f'번호 : {student_scores[1][0]}')
print(f'이름 : {student_scores[1][1]}')
print(f'국어 : {student_scores[1][2]}')
print(f'영어 : {student_scores[1][3]}')
print(f'수학 : {student_scores[1][4]}')

print(f'번호 : {student_scores[2][0]}')
print(f'이름 : {student_scores[2][1]}')
print(f'국어 : {student_scores[2][2]}')
print(f'영어 : {student_scores[2][3]}')
print(f'수학 : {student_scores[2][4]}')


# 1, '일길동', 100, 100, 100
# 2, '이길동', 90, 90, 90
# 3, '삼길동', 90, 90, 90

for i in range(len(student_scores)):
    for j in range(len(student_scores[i])):
        print(f'{student_scores[i][j]}', end = '\t')
    print()