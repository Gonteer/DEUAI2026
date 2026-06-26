pp = []
while True :
    n  = input('학생 이름?')
    s1 = int(input('국어 성적?'))
    s2 = int(input('영어 성적?'))
    s3 = int(input('수학 성적?'))

    to = s1 + s2 + s3 #합계
    avg = to / 3

    pp.append([n,s1,s2,s3,to,round(avg,2)])

    print('당신의 과목 합계 점수는', to, '점, 평균은',avg,'점 입니다.')
    print('당신은',end=' ')

    if avg >= 90 :
        print('A',end='')
    elif avg >= 80 :
        print('B',end='')
    elif avg >= 70 :
        print('C',end='')
    elif avg >= 60 :
        print('D',end='')
    else :
        print('F',end='')

    print('입니다')

    ans = input('계속 입력하시겠습니까(y/n)?')
    if ans == 'n' :
        print('모두 입력 완료!!\n')
        break

print('*'*30)
print('이름\t 국어\t 영어\t 수학\t 합계\t 평균\t')
print('*'*30)
for i in pp :
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t')
print('*'*30)
