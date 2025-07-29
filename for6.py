

# for i in range(1, 10, 1):
#     for y in range(2, 10, 1):
#         print (f'{y} * {i} = {y * i}', end='\t')
#     print()


for i in range(1, 10):
    for y in range(2, 10):
        print(f'{y} * {i} = {y * i:2}', end='    ')
    print()