scores = [90,88,34,56,67,78,88,60,59,100]

for i in range(0, len(scores), 1):
    if scores[i] < 60:
        continue

    print(f'{i + 1}번 학생 축하합니다. 합격입니다.')

         