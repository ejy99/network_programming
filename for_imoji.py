print('1. ☆\n2. ★\n3. #')
mode = int(input('모드를 선택 하시오: '))
length = int(input('길이를 입력 하시오: '))

if mode == 1:
    for i in range(length):
        print('☆')
elif mode == 2:
    for i in range(length):
        print('★')
elif mode == 3:
    for i in range(length):
        print('#')
else :
    print('재실행하여 모드를 다시 선택 하시오:')