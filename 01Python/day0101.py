bmis = list() #[]
while True:
    t = float(input('당신의 키는(m)? '))
    w = float(input('당신의 몸무게(kg)는? '))
    #bmi = 100 / (1.84**2)
    #BMI 계산식
    bmi = w / (t**2)
    print('당신의 BMI',bmi,'입니다.')

    bmis.append(bmi) #bmis에 현재 bmi추가
    '''
    if bmi >= 25.0 :
        print('당신은 비만 입니다')
    else :
        print('당신은 정상 입니다.')
    '''
    print('당신은 ', end='')

    if bmi >= 35 :
        print('고도비만',end='')
    elif bmi >= 30 :
        print('2단계 비만',end='')
    elif bmi >= 25 :
        print('1단계 비만',end='')
    elif bmi >= 23 :
        print('비만전단계(과체중)',end='')
    elif bmi >= 18.5 :
        print('정상',end='')
    else :
        print('저체중',end='')

    print('입니다.')
    #추가 소스코드
    ans = input('계속 입력 하시겠습니까?(y/n)')

    if ans == 'n' :
        print('프로그램 종료')
        break

print(len(bmis),'명의 데이터를 입력 받았습니다')
print('입력하신 BMI의 평균은 ',sum(bmis)/len(bmis),'입니다')
