pp = list() #[]
while True : 
    n = input('당신의 이름은?')
    t = float(input('당신의 키(m)는?'))
    w = float(input('당신의 몸무게(kg)는?'))
    bmi = w / (t ** t)
    print('당신의 BMI:',bmi)
    pp.append([n,t,w,round(bmi,2)]) #pp에 추가됨

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
        
    #추가된 부분
    ans = input('계속 입력하시겠습니까(y/n)?')
    if ans == 'n' :
        print('입력완료!!!')
        break

#사람 정보 출력
print('성명\t 키\t 몸무게\t BMI\t')
print('*' * 30)
for i in pp :
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])
print('*' * 30)
