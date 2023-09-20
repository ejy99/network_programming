ListA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ListB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ListC = []  # 빈 리스트 생성

i = 0
j = 0

for k in range(1, 5, 1):
    j += k
    ListC = ListC + ListA[i:j] + ListB[i:j] # ListC에 [0:1], [1:3], [3:6], [6:10] 순서로 추가
    i += k

print('ListA = ' + str(ListA))
print('ListB = ' + str(ListB))
print('ListC = ' + str(ListC))


