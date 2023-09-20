weight = int(input('몸무게를 입력해 주세요: '))
tall = float(input('자신의 키를 입력해 주세요: '))
bmi = weight / (tall ** 2)
print('BMI 지수: ' + str(bmi))