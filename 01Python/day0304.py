def bmic(t,w) :
    bmi = w / (t**2)
    return round(bmi,2)

def rst(bmi) :
    rstr = ''
    if bmi >= 35 :
        rstr = '고도비만'
    elif bmi >= 30 :
        rstr = '2단계 비만'
    elif bmi >= 25 :
        rstr = '1단계 비만'
    elif bmi >= 23 :
        rstr = '비만전단계(과체중)'
    elif bmi >= 18.5 :
        rstr = '정상'
    else :
        rstr = '저체중'
    return rstr 
        

bmis = dict()
while True:
    n = input('당신의 이름은?')
    t = float(input('당신의 키는(m)? '))
    w = float(input('당신의 몸무게(kg)는? '))

    #bmi = w / (t**2)
    bmi = bmic(t,w)

    print('당신의 BMI',bmi,'입니다.')

    r = rst(bmi) 
    
    print('당신은 ',r, '입니다.')

    bmis[n] = [t,w,bmi,r] #새로 추가
    
    #추가 소스코드
    ans = input('계속 입력 하시겠습니까?(y/n)')

    if ans == 'n' :
        print('프로그램 종료')
        break

#dict 자료형 전체 출력
print('이름\t 키\t 몸무게\t BMI\t BMI결과\t')
print('*' * 30)
for k,v in bmis.items() :
    print(k,'\t',v[0],'\t',v[1],'\t',v[2],'\t',v[3])
