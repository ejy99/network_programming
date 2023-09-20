work_score = int(input('과제: '))
middle_score = int(input('중간: '))
last_score = int(input('기말: '))
average_score = (work_score + middle_score + last_score) / 3
print('평균: ' + str(average_score))

if average_score >= 90 :
    print('A학점 입니다.')
elif average_score < 90 and average_score >= 80 :
    print('B학점 입니다.')
elif average_score < 80 and average_score >= 70 :
    print('C학점 입니다.')
elif average_score < 70 and average_score >= 60 :
    print('D학점 입니다.')
else :
    print('F학점 입니다.')