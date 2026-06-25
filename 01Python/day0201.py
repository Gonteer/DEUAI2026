t = float(input('당신의 키(m)는?'))
w = float(input('당신의 몸무게(kg)는?'))
bmi = w / (t ** t)
print('당신의 BMI:',bmi)

#if bmi >= 25 :
#    print('당신은 비만입니다.')
#else :
#    print('당신은 보통입니다.')

if bmi >= 35 :
    print('당신은 고도비만 입니다.')
elif bmi >= 25 :
    print('당신은 비만 입니다.')
elif bmi >= 23 :
    print('당신은 과체중 입니다.')
elif bmi >= 18.5 :
    print('당신은 보통 입니다.')
else :
    print('당신은 저체중 입니다.')
